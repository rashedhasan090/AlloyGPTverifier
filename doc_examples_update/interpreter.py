from typing import List


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


def remove_specification_part(line):
    # Check if the line contains "in" and "specification:"
    start_index = line.find(" in ")
    end_index = line.find("specification:")

    if start_index != -1 and end_index != -1:
        return line[:start_index] + line[end_index + len("specification:") :]
    else:
        return line


def remove_compilation_error_line(compilation_error_message):
    lines = compilation_error_message.split("\n")
    new_lines = []

    for line in lines:
        # Check if the line contains "in" and "specification:"
        line = remove_specification_part(line)

        # Check if the line starts with "in" and ends with "specification:"
        if line.startswith("in") and line.endswith("specification:"):
            continue

        # Replace "Warning" with "generates a compilation error at"
        line = line.replace("Warning", "generates a compilation error at")

        new_lines.append(line)

    return "\n".join(new_lines)


def process_Alloy_json_report(json_data) -> List[str]:
    output_lines = []

    # Process counterexamples
    counterexamples = json_data.get("counterexamples", [])
    if counterexamples:
        for item in counterexamples:
            cntr_cmd = item.get("cntr_cmd", "")
            cntr_cmd = cntr_cmd.replace("expect 0", "").strip()

            counterexample_msg = item.get("counterexample_msg", "")
            counterexample = item.get("counterexample", "")

            # Extract assertion name by excluding the word "Check" if present
            assertion_name = remove_dollar_sign(cntr_cmd.replace("Check", "").strip())

            # Check for "Counterexample not found" and print the appropriate message
            if counterexample.lower() == "no":
                output_lines.append(
                    f"""
                    Executing command [{cntr_cmd}] of the proposed Alloy model,
                    Alloy analyzer found no counterexample, indicating assert
                    {assertion_name} is valid
                    """
                )
            else:
                # Add the execution command and counterexample message to output_lines
                output_lines.append(
                    f"""
                    Executing command [{cntr_cmd}] of the proposed Alloy model,
                    Alloy analyzer found a counterexample, Indicating assert
                    {assertion_name} is violated by this counterexample:\n
                    """
                )

                # Exclude unwanted lines and prefixes
                counterexample_msg_lines = [
                    remove_dollar_sign(line.replace("this/", ""))
                    for line in counterexample_msg.split("\n")
                    if line and "Counterexample found which means that" not in line
                ]
                output_lines.extend(counterexample_msg_lines)

    # Process instances
    instances = json_data.get("instances", [])
    if instances:
        for item in instances:
            instance_cmd = item.get("instance_cmd", "")
            inst = item.get("instances", "")

            # Extract instance name by excluding the word "Run" if present
            instance_name = remove_dollar_sign(instance_cmd.replace("Run", "").strip())

            if inst.lower() == "yes":
                output_lines.append(
                    f"""
                    Executing command [{instance_cmd}] of proposed Alloy model, Alloy
                    analyzer generates a valid instance, indicating the model is
                    consistent and pred {instance_name} is satisfied.\n
                    """
                )
            else:
                output_lines.append(
                    f"""
                    Executing command [{instance_cmd}] of proposed Alloy model, Alloy
                    analyzer does not generate a valid instance, indicating the model is
                    inconsistent and pred {instance_name} is not satisfied.\n
                    """
                )

    # Process error
    error = json_data.get("error", "")
    if error:
        # Check if the error starts with "Warning Line" (compilation error)
        if "Warning Line" in error:
            # Extract line number, and column from the error message
            line_number, column_number, _ = extract_file_info(error)

            # Print the compilation error message without filename, line, and column
            compilation_error_message = remove_dollar_sign(
                " ".join(error.split(" ")[5:]).strip()
            )
            compilation_error_message = remove_compilation_error_line(
                compilation_error_message
            )
            error_lines = compilation_error_message.split("\n")
            new_err_message = ""
            for line in error_lines:
                if "als" not in line:
                    new_err_message = new_err_message + "\n" + line

            output_lines.append(
                f"""Compiling the proposed Alloy model generates a compilation error at
                  Line {line_number}, Column {column_number}: {new_err_message}"""
            )

        elif error.startswith("Type error in"):
            # Extract line number, and column from the error message
            line_number, column_number, _ = extract_file_info(error)

            # Print the type error message without filename
            error_lines = error.split("\n")
            new_err_message = ""
            for line in error_lines:
                if not line.startswith("\tat") and "als" not in line:
                    new_err_message = new_err_message + "\n" + line
            print(new_err_message)
            output_lines.append(
                f"""Compiling the proposed Alloy model generates a type error at Line
                {line_number}, Column {column_number}: {new_err_message}"""
            )

        else:
            # Syntax error
            error_lines = error.split("\n")
            # Extract syntax error message
            syntax_error_message = remove_dollar_sign(
                " ".join(error.split(" ")[5:]).strip()
            )
            error_lines = syntax_error_message.split("\n")
            syntax_error_message = (
                error_lines[0] + "\n" + error_lines[1] + "\n" + error_lines[2]
                if error_lines
                else ""
            )
            output_lines.append(
                f"""Compiling the proposed Alloy model generates a syntax error at line
                  {syntax_error_message}"""
            )

    return output_lines