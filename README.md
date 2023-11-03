# AlloyGPTverifier
Our Alloy specification verifier with Alloy API's, which helps us to 
run Alloy specification swiftly and integrate it with otyer services. 


## Usage

- git clone [project]
- Go to the solver_new_version folder.
- Execute Bulk_exec.sh (./Bulk_exec.sh) in your terminal.
- The example .als files will be executed and output will be saved into a .json file.

- Alternatively "java -jar solver.jar $.als file" will do the job.

## Model

- The alloy 4.2 folder contains the project files (Intellij IDEA).
- "GPTEvaluator" is the main class in "tmp" folder.
- Alloy API files can also be found.

## Building .jar from source 

- git clone [project]
- Import the project into IntelliJ IDEA.
- After the project is successfully imported you can see all the folders in the Project Explorer. 
- Go to the "tmp" folder.
- "GPTEvaluator" is the main class.
- Now go to File > Project Structure > Artifacts. 
- You will see a "+" sign in the second column. 
- Click on the sign > select JAR > "From module with dependencies"
- Now select the module (alloy4.2) and select the main class which is "GPTEvaluator".
- Now save changes by clicking "OK".
- Now go to the "Build" option from the Menu bar.
- Click on Build Artifacts.
- select the jar to be created and, click Build on the "Action" segment. 
- You will be able to identify the .jar in "Out" > "artifacts". 




