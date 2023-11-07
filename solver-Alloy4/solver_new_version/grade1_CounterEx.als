<alloy builddate="2012-09-25 15:54 EDT">

<instance bitwidth="0" maxseq="0" command="Check repair_assert_1" filename="">

<sig label="seq/Int" ID="0" parentID="1" builtin="yes">
</sig>

<sig label="Int" ID="1" parentID="2" builtin="yes">
</sig>

<sig label="String" ID="3" parentID="2" builtin="yes">
</sig>

<sig label="this/Student" ID="4" parentID="5">
   <atom label="Student$0"/>
   <atom label="Student$1"/>
</sig>

<sig label="this/Professor" ID="6" parentID="5">
   <atom label="Professor$0"/>
</sig>

<sig label="this/Person" ID="5" parentID="2" abstract="yes">
</sig>

<sig label="this/Class" ID="7" parentID="2">
   <atom label="Class$0"/>
   <atom label="Class$1"/>
   <atom label="Class$2"/>
</sig>

<field label="assistant_for" ID="8" parentID="7">
   <tuple> <atom label="Class$0"/> <atom label="Student$0"/> </tuple>
   <tuple> <atom label="Class$1"/> <atom label="Student$1"/> </tuple>
   <tuple> <atom label="Class$2"/> <atom label="Student$0"/> </tuple>
   <tuple> <atom label="Class$2"/> <atom label="Student$1"/> </tuple>
   <types> <type ID="7"/> <type ID="4"/> </types>
</field>

<field label="instructor_of" ID="9" parentID="7">
   <tuple> <atom label="Class$0"/> <atom label="Professor$0"/> </tuple>
   <tuple> <atom label="Class$1"/> <atom label="Professor$0"/> </tuple>
   <tuple> <atom label="Class$2"/> <atom label="Professor$0"/> </tuple>
   <types> <type ID="7"/> <type ID="6"/> </types>
</field>

<sig label="this/Assignment" ID="10" parentID="2">
   <atom label="Assignment$0"/>
   <atom label="Assignment$1"/>
   <atom label="Assignment$2"/>
</sig>

<field label="associated_with" ID="11" parentID="10">
   <tuple> <atom label="Assignment$0"/> <atom label="Class$2"/> </tuple>
   <tuple> <atom label="Assignment$1"/> <atom label="Class$1"/> </tuple>
   <tuple> <atom label="Assignment$2"/> <atom label="Class$2"/> </tuple>
   <types> <type ID="10"/> <type ID="7"/> </types>
</field>

<field label="assigned_to" ID="12" parentID="10">
   <tuple> <atom label="Assignment$0"/> <atom label="Student$0"/> </tuple>
   <tuple> <atom label="Assignment$0"/> <atom label="Student$1"/> </tuple>
   <tuple> <atom label="Assignment$1"/> <atom label="Student$0"/> </tuple>
   <tuple> <atom label="Assignment$1"/> <atom label="Student$1"/> </tuple>
   <tuple> <atom label="Assignment$2"/> <atom label="Student$0"/> </tuple>
   <tuple> <atom label="Assignment$2"/> <atom label="Student$1"/> </tuple>
   <types> <type ID="10"/> <type ID="4"/> </types>
</field>

<sig label="univ" ID="2" builtin="yes">
</sig>

<skolem label="$repair_assert_1_s" ID="13">
   <tuple> <atom label="Student$1"/> </tuple>
   <types> <type ID="5"/> </types>
</skolem>

<skolem label="$repair_assert_1_a" ID="14">
   <tuple> <atom label="Assignment$2"/> </tuple>
   <types> <type ID="10"/> </types>
</skolem>

</instance>

</alloy>
