package alloyrepair;

import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

public class JsonHelper {
    public static JsonObject createJsonObject(String cntrCmd, String counterexample, String counterexampleMsg,
            String instanceCmd, String instances, String instanceMsg, String error) {
        JsonObject jsonObject = new JsonObject();

        // Initialize the arrays without adding empty records
        jsonObject.add("counterexamples", new JsonArray());
        jsonObject.add("instances", new JsonArray());
        jsonObject.addProperty("error", error);

        return jsonObject;
    }

    // Method to add a new counterexample item
    public static void addCounterexample(JsonObject jsonObject, String cntrCmd, String counterexample,
            String counterexampleMsg) {
        JsonArray counterexamplesArray = jsonObject.getAsJsonArray("counterexamples");
        JsonObject newCounterexampleItem = new JsonObject();
        newCounterexampleItem.addProperty("cntr_cmd", cntrCmd);
        newCounterexampleItem.addProperty("counterexample", counterexample);
        newCounterexampleItem.addProperty("counterexample_msg", counterexampleMsg);
        counterexamplesArray.add(newCounterexampleItem);
    }

    // Method to add a new instance item
    public static void addInstance(JsonObject jsonObject, String instanceCmd, String instances, String instanceMsg) {
        JsonArray instancesArray = jsonObject.getAsJsonArray("instances");
        JsonObject newInstanceItem = new JsonObject();
        newInstanceItem.addProperty("instance_cmd", instanceCmd);
        newInstanceItem.addProperty("instances", instances);
        newInstanceItem.addProperty("instance_msg", instanceMsg);
        instancesArray.add(newInstanceItem);
    }
}
