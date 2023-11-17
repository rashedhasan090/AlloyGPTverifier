import os
import json

def remove_dollar_sign(text):
    return text.replace("$", "")

def extract_file_info(error_message):
    # Extract line number, and column from the error message
    error_parts = error_message.split(" ")
    line_number = error_parts[2]
    column_number = error_parts[4]

    # Extract filename from the error message
    error_filename = remove_dollar_sign(error_parts[-1].strip())

    return line_number, column_number, error_filename

def process_json(json_data, filename):
    output_lines = []


    filename = remove_dollar_sign(filename.replace("_alloyAnalyzerReport", "").strip())

    # Process counterexamples
    counterexamples = json_data.get("counterexamples", [])
    if counterexamples:
        output_lines.append("")
        for item in counterexamples:
            cntr_cmd = item.get("cntr_cmd", "")
            cntr_cmd = cntr_cmd.replace("expect 0", "")

            counterexample_msg = item.get("counterexample_msg", "")

            # Extract assertion name by excluding the word "Check" if present
            assertion_name = remove_dollar_sign(cntr_cmd.replace("Check", "").strip())

            # Exclude "_alloyAnalyzerReport" from command and filename
            cntr_cmd = remove_dollar_sign(cntr_cmd.replace("_alloyAnalyzerReport", "").strip())
            # filename = remove_dollar_sign(filename.replace("_alloyAnalyzerReport", "").strip())

            # Check for "Counterexample not found" and print the appropriate message
            if "Counterexample not found" in counterexample_msg:
                output_lines.append(f"Executing command [{cntr_cmd}] of Alloy model {filename}.als, Alloy analyzer found no counterexample,\n")
                output_lines.append(f"indicating assert {assertion_name} is valid.\n")
                output_lines.append(f"\n")
            else:
                # Add the execution command and counterexample message to output_lines
                output_lines.append(f"Executing command [{cntr_cmd}] of the Alloy model {filename}.als, Alloy analyzer found a counterexample,")
                output_lines.append(f"Indicating assert {assertion_name} is violated by this counterexample:\n")
                output_lines.append(f"\n")

                # Exclude unwanted lines and prefixes
                counterexample_msg_lines = [
                    remove_dollar_sign(line.replace("Counterexample found which means that", "").replace("this/", ""))
                    for line in counterexample_msg.split('\n')
                    if line and "Counterexample found which means that" not in line
                ]
                output_lines.extend(counterexample_msg_lines)

                # Include the line indicating assert violation


    # Process instances
    instances = json_data.get("instances", [])
    if instances:
        output_lines.append("")
        for item in instances:
            instance_cmd = item.get("instance_cmd", "")
            instance_msg = item.get("instance_msg", "")

            # Extract instance name by excluding the word "Run" if present
            instance_name = remove_dollar_sign(instance_cmd.replace("Run", "").strip())

            # Add the execution command and instance message to output_lines
            output_lines.append(f"Executing command [{instance_cmd}] of Alloy model {filename}.als, Alloy analyzer generates a valid instance,")
            output_lines.append(f"indicating the model is consistent and pred {instance_name} is satisfied.\n")
            output_lines.append(f"\n")


    # Process error
    error = json_data.get("error", "")
    if error:
        output_lines.append("")
        # Check if the error starts with "Warning Line" (compilation error)
        if "Warning Line" in error:
            # Extract line number, and column from the error message
            line_number, column_number, _ = extract_file_info(error)

            # Print the compilation error message without filename, line, and column
            compilation_error_message = remove_dollar_sign(' '.join(error.split(" ")[5:]).strip())
            error_lines = compilation_error_message.split('\n')
            new_err_message = ""
            for line in error_lines:
                if "als" not in line:

                    new_err_message = new_err_message + "\n" + line

            output_lines.append(f"Compiling the Alloy model {filename}.als generates a compilation error at Line {line_number}, Column {column_number}: {new_err_message}")

        elif error.startswith("Type error in"):
            # Extract line number, and column from the error message
            line_number, column_number, _ = extract_file_info(error)

            # Print the type error message without filename
            # type_error_message = remove_dollar_sign(' '.join(error.split(" ")[5:]).strip())
            error_lines = error.split('\n')
            new_err_message = ""
            for line in error_lines:
                if not line.startswith("\tat") and "als" not in line :
                    new_err_message = new_err_message + "\n" + line
            print(new_err_message)
            # type_error_message = error_lines[0]+ "\n"+ error_lines[1] + "\n" + error_lines[1] if error_lines else ""
            # type_error_message = error_lines[0]+ "\n"+ error_lines[1] + "\n" + error_lines[2] if error_lines else ""
            output_lines.append(f"Compiling the Alloy model {filename}.als generates a type error at Line {line_number}, Column {column_number}: {new_err_message}")

        else:
            # Syntax error
            error_lines = error.split('\n')
            # Extract syntax error message
            syntax_error_message = remove_dollar_sign(' '.join(error.split(" ")[5:]).strip())
            error_lines = syntax_error_message.split('\n')
            syntax_error_message = error_lines[0]+ "\n"+ error_lines[1] + "\n" + error_lines[2] if error_lines else ""
            output_lines.append(f"Compiling the Alloy model {filename}.als generates a syntax error at line {syntax_error_message}")

    # Save the output to a text file
    output_filename = os.path.join(os.getcwd(), f"{filename}_output.txt")
    with open(output_filename, "a") as output_file:
        output_file.write("\n".join(output_lines) + "\n")

def process_all_json_files():
    current_directory = os.getcwd()
    for filename in os.listdir(current_directory):
        if filename.endswith(".json"):
            with open(os.path.join(current_directory, filename), "r") as json_file:
                json_data = json.load(json_file)
                process_json(json_data, os.path.splitext(filename)[0])

# Process all JSON files in the current working directory
process_all_json_files()
