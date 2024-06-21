import os

def list_directory_contents(path):
    try:
        # Ensure path is a valid directory
        if os.path.isdir(path):
            print(f"Contents of directory '{path}':")
            for item in os.listdir(path):
                print(item)
        else:
            print(f"Error: '{path}' is not a valid directory.")
    except OSError as e:
        print(f"Error: {e}")

# Prompt user for directory path
directory_path = input("Enter the directory path: ")

# Call function to list directory contents
list_directory_contents(directory_path)