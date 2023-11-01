package tmp;

import edu.mit.csail.sdg.alloy4.A4Reporter;
import edu.mit.csail.sdg.alloy4.Err;
import edu.mit.csail.sdg.alloy4.ErrorWarning;
import edu.mit.csail.sdg.alloy4compiler.ast.*;
import edu.mit.csail.sdg.alloy4compiler.parser.CompModule;
import edu.mit.csail.sdg.alloy4compiler.parser.CompUtil;
import edu.mit.csail.sdg.alloy4compiler.translator.A4Options;
import edu.mit.csail.sdg.alloy4compiler.translator.A4Solution;
import edu.mit.csail.sdg.alloy4compiler.translator.TranslateAlloyToKodkod;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintStream;
import java.text.SimpleDateFormat;
import java.util.*;

public class GPTEvaluator {
    Module root = null;
    A4Solution ans = null;
    protected String result;
    protected ArrayList<String> resultsArray = new ArrayList<String>();
    static int solutionNo = 1;
    static int maxSol = 10000000;

    FileOutputStream oFile;
    static PrintStream pPRINT = null;

    HashMap<String, String> uniqueSkolems;
    HashMap<String, HashSet<String>> skolemsHashMAp;
    HashMap<String, Integer> src,dst,intents,perm;

    //[src-dst,Sol#]
    HashMap<String, HashSet<String>> distinctSrcDst;

    public GPTEvaluator() {
    }

    /**
     * This object performs expression evaluation.
     *
     * @param args AlloyFile Query
     */

    public static void main(String args[]) throws FileNotFoundException {




        GPTEvaluator e = new GPTEvaluator();
        FileOutputStream oStream = null;
        String outputFile = args[0].substring(0, args[0].length() - 4) + "_Sol.txt";
        oStream = new FileOutputStream(outputFile);
        PrintStream f = new PrintStream(oStream, true);
        System.setOut(f);

        try {
            e.callAlloyEngine(args[0]);
        } catch (Exception err) {
            err.printStackTrace();
            pPRINT.println(err);
        }
        //e.query(args[1]);

    }

    public static String instanceParser(String sol, Map<String, Sig> sigs) {
        String[] lines = sol.split("\n");
        for (String line : lines) {
            String firstPart = line.split("=")[0];
            if (firstPart.contains("<:")){
                System.out.println(line);
            }else{
                boolean flag =false;
                for (Sig sig: sigs.values()){
                    if (sig.toString().equals(firstPart)){
                        flag = true;
                        break;
                    }
                }
                if (flag){
                    System.out.println(line);
                }

            }

//            if (line.contains("this")){
//                System.out.println(line);
//            }

        }
        return sol;

    }

    public void callAlloyEngine(String model) throws Err, FileNotFoundException {
        String trimmedFilenameAllSols = model.substring(0, model.length() - 4) + "_Sol.txt";
        //I need save the output of instanceParser in the same _Sol.txt file.

        oFile = new FileOutputStream(trimmedFilenameAllSols, false);
        pPRINT = new PrintStream(oFile);
        uniqueSkolems = new HashMap<String, String>();
        skolemsHashMAp = new HashMap<String, HashSet<String>>();

        src = new HashMap<String, Integer>();
        dst = new HashMap<String, Integer>();
        intents = new HashMap<String, Integer>();
        perm = new HashMap<String, Integer>();

        distinctSrcDst = new HashMap<String, HashSet<String>>(); //new HashMap<String, Integer>();

        boolean isFinished = false;
        A4Reporter rep = new A4Reporter() {
            @Override
            public void warning(ErrorWarning msg) {
                System.out.print("Relevance Warning:\n" + (msg.toString().trim()) + "\n\n");
                System.out.flush();
            }
        };
        root = CompUtil.parseEverything_fromFile(rep, null, model);
//        for (:root.getOld2fields()
//             ) {
//
//        }
//        System.out.println(root.getSigs());
        System.out.println("----------------");
        // Choose some default options for how you want to execute the commands
        A4Options options = new A4Options();
        options.solver = A4Options.SatSolver.SAT4J; //.KK;//.MiniSatJNI; //.MiniSatProverJNI;//.SAT4J;
        options.symmetry = 20;
        options.skolemDepth = 1;

        long now, start = System.currentTimeMillis();
        SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
        sdf.setTimeZone(TimeZone.getTimeZone("UTC"));
        Date startTime = new Date(start);


        for (Command command : root.getAllCommands()) {
            if (command.toString().contains("Check"))
            {

                System.out.println("Command " + command + ": (" + sdf.format(startTime) + ")");
//                System.out.println("Command " + command + ": (" + sdf.format(startTime) + ")");
                try {
                    ans = TranslateAlloyToKodkod.execute_command(rep, root.getAllReachableSigs(), command, options);
                } catch (Err err) {
                    err.printStackTrace();
                }
                for (ExprVar a : ans.getAllAtoms()) {
                    root.addGlobal(a.label, a);
                }
                for (ExprVar a : ans.getAllSkolems()) {
                    root.addGlobal(a.label, a);
                }

                if (ans.satisfiable()) {
                    System.out.println("Counterexample found which means that " + command + " assertion is invalid");
//                    System.out..println("Counterexample found which means that " + command + " assertion is invalid");
                    //Not only print the statement but I need to export the counterexample in a text file. The name of the file is the same as the model file but with a different extension.
                    //String trimmedFilenameCounterEx = model.substring(0, model.length() - 4) + "_CounterEx.txt";
                    // I actually need to export the counterexample in text format not in <skolem> rather than in text where the counterexample starts with

//                    String trimmedFilenameCounterEx = model.substring(0, model.length() - 4) + "_CounterEx.als";
//                    System.out.println("Counterexample found in file: " + trimmedFilenameCounterEx);
//                    pPRINT.println("Counterexample found in file: " + trimmedFilenameCounterEx);
                    String parsedInstance = instanceParser(ans.toString(), root.getSigs());
//                    try {
////                        System.out.println(ans);
//                        String parsedInstance = instanceParser(ans.toString(), root.getSigs());
////                        System.out.println(parsedInstance);
////                        ans.writeXML(trimmedFilenameCounterEx);
//
//                    } catch (Err err) {
//                        err.printStackTrace();
//                    }
                    System.out.println("\n-----------------------------------------");
//                    pPRINT.println("\n-----------------------------------------");


                } else {
                    System.out.println("Counterexample not found which means that " + command + " is valid");
//                    pPRINT.println("Counterexample not found which means that " + command + " is valid");
                }


                System.out.println("\n=========================================");


//                pPRINT.println("\n=========================================");

            }else if (command.toString().contains("Run"))
            {

                System.out.println("Command " + command + ": (" + sdf.format(startTime) + ")");
//                pPRINT.println("Command " + command + ": (" + sdf.format(startTime) + ")");
                try {
                    ans = TranslateAlloyToKodkod.execute_command(rep, root.getAllReachableSigs(), command, options);
                } catch (Err err) {
                    err.printStackTrace();
//                    pPRINT.println(err.msg);
                }
                for (ExprVar a : ans.getAllAtoms()) {
                    root.addGlobal(a.label, a);
                }
                for (ExprVar a : ans.getAllSkolems()) {
                    root.addGlobal(a.label, a);
                }

                if (ans.satisfiable()) {
                    System.out.println("Instance found which means that the specification is consistent");
//                    pPRINT.println("Instance found which means that the specification is consistent");
                } else {
                    System.out.println("Instance not found which means that the specification is not consistent.");
//                    pPRINT.println("Instance not found which means that the specification is not consistent.");
                    System.out.println("\n-----------------------------------------");
                }

                System.out.println("\n=========================================");


//                pPRINT.println("\n=========================================");

            }
        }

    }

    private String printTime(long start) {
        StringBuilder sb = new StringBuilder();
        long now;
        now = System.currentTimeMillis();
        sb.append(//"Sol: " + solutionNo + " " +
                "within: " + (now - start) / 1000 + "sec.");
        sb.append("\n-----------------------------------------");
        return sb.toString();
    }





    protected void solve(String AlloyFile) {
        // Alloy4 sends diagnostic messages and progress reports to the A4Reporter.
        // By default, the A4Reporter ignores all these events (but you can extend the A4Reporter to display the event for the user)
        A4Reporter rep = new A4Reporter() {
            // For example, here we choose to display each "warning" by printing it to System.out
            @Override
            public void warning(ErrorWarning msg) {
                System.out.print("Relevance Warning:\n" + (msg.toString().trim()) + "\n\n");
                System.out.flush();
            }
        };


        try {
            root = CompUtil.parseEverything_fromFile(rep, null, AlloyFile);
        } catch (Err err) {

            err.printStackTrace();
        }
        A4Options options = new A4Options();
        options.solver = A4Options.SatSolver.SAT4J;//.KK;//.MiniSatJNI; //.MiniSatProverJNI;//.SAT4J;

        options.symmetry = 20;
        options.skolemDepth = 1;

        for (Command command : root.getAllCommands()) {
            // Execute the command
            System.out.println("============ Command " + command + ": ============");
            try {
                ans = TranslateAlloyToKodkod.execute_command(rep, root.getAllReachableSigs(), command, options);
            } catch (Err err) {
                err.printStackTrace();
            }
            for (ExprVar a : ans.getAllAtoms()) {
                root.addGlobal(a.label, a);
            }
            for (ExprVar a : ans.getAllSkolems()) {
                root.addGlobal(a.label, a);
            }
        }
    }
}
