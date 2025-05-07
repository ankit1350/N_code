import os
import shutil

# Create a new directory
def create_directory(path):
    try:
        os.makedirs(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")
    except Exception as e:
        print(f"Error creating directory '{path}': {e}")

# List all files and directories in a given path
def list_directory_contents(path):
    try:
        contents = os.listdir(path)
        print(f"Contents of '{path}': {contents}")
        return contents
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
    except Exception as e:
        print(f"Error listing contents of '{path}': {e}")

# Delete a directory
def delete_directory(path):
    try:
        shutil.rmtree(path)
        print(f"Directory '{path}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
    except Exception as e:
        print(f"Error deleting directory '{path}': {e}")

# Rename a directory
def rename_directory(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        print(f"Directory renamed from '{old_path}' to '{new_path}'.")
    except FileNotFoundError:
        print(f"Directory '{old_path}' not found.")
    except Exception as e:
        print(f"Error renaming directory '{old_path}': {e}")

# Example usage
if __name__ == "__main__":
    create_directory("example_dir")
    list_directory_contents(".")
    rename_directory("example_dir", "renamed_dir")
    delete_directory("renamed_dir")