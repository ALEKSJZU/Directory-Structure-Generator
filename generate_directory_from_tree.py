import os
import tkinter as tk
from tkinter import filedialog
from tkinter.simpledialog import askstring

def read_tree_from_file(file_path):
    with open(file_path, 'r') as file:
        tree = file.read()
    return tree

def create_from_tree(root_name, custom_path):
    base_path = os.path.join(os.path.abspath(custom_path), root_name) if custom_path else os.path.abspath(root_name)
    os.makedirs(base_path, exist_ok=True)
    return base_path

def create_structure(tree, base_path):
    current_path = base_path
    path_levels = {0: base_path}  # Initialize the root path

    for line in tree.strip().split('\n'):
        indent_level = (len(line) - len(line.lstrip(' |'))) // 2
        name = line.strip(' |+-')
        is_dir = '+' in line

        # Ensure current_path is correctly updated for each indentation level
        if indent_level in path_levels:
            current_path = path_levels[indent_level]
        else:
            # If the expected level isn't directly available, use the highest known level
            # This handles skipped levels gracefully
            current_path = path_levels[max(path_levels.keys())]

        if is_dir:
            new_dir_path = os.path.join(current_path, name)
            os.makedirs(new_dir_path, exist_ok=True)
            # Update the path for the current level and remove any higher levels that might have been incorrectly inferred
            path_levels[indent_level] = new_dir_path
            # This loop cleans up any 'future' paths that might not be valid after adding a new branch in the tree
            for key in list(path_levels.keys()):
                if key > indent_level:
                    del path_levels[key]
        else:
            file_path = os.path.join(current_path, name)
            open(file_path, "a").close()

def process_tree_from_file(file_path, root_name, custom_path=None):
    tree = read_tree_from_file(file_path)
    base_path = create_from_tree(root_name, custom_path)
    create_structure(tree, base_path)

def run_gui():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask the user to select the directory tree file
    file_path = filedialog.askopenfilename(
        title="Select the Directory Tree File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if not file_path:  # User cancelled the file selection
        return

    # Ask for the root name of the project
    root_name = askstring("Input", "Enter the root name for the project:")
    if not root_name:  # User cancelled or entered no input
        return

    # Ask for the custom path where the directory should be created
    custom_path = filedialog.askdirectory(title="Select the Custom Path for the Directory Structure")
    if not custom_path:  # User cancelled the directory selection
        return

    # Process the tree from the file with the provided inputs
    process_tree_from_file(file_path, root_name, custom_path)

    # Show a completion message
    tk.messagebox.showinfo("Success", "The directory structure has been created successfully!")

if __name__ == "__main__":
    run_gui()
