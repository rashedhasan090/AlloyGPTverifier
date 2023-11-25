import os

def remove_text_files():
    current_directory = os.getcwd()
    for filename in os.listdir(current_directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(current_directory, filename)
            os.remove(file_path)
            print(f"Removed: {file_path}")

if __name__ == "__main__":
    remove_text_files()
