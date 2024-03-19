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

def read_tree_from_file(file_path):
    with open(file_path, 'r') as file:
        tree = file.read()
    return tree

def create_from_tree(root_name, custom_path):
    base_path = os.path.join(os.path.abspath(custom_path), root_name) if custom_path else os.path.abspath(root_name)
    os.makedirs(base_path, exist_ok=True)
    return base_path


def create_structure(tree, base_path):
    path_levels = {0: base_path}  # Initialize the root path with the base directory
    last_indent_level = 0  # Track the last line's indent level for comparison

    for line in tree.strip().split('\n'):
        indent_count = 0
        cleaned_line = line.lstrip("|")

        # Counting spaces and '+' or '-' signs to determine indentation level
        for char in cleaned_line:
            if char in [' ', '+', '-']:
                indent_count += 1
            elif char.isalnum():
                break

        indent_level = indent_count // 2
        name = line.strip(' |+-')
        is_dir = '+' in line

        # Handling the hierarchical structure based on the comparison of indent levels
        if indent_level > last_indent_level:
            # Child of the previous line
            parent_path = path_levels[last_indent_level]
        elif indent_level == last_indent_level:
            # Sibling of the previous line
            parent_path = os.path.dirname(path_levels[last_indent_level])
        else:
            # Determine how many levels to go up based on the difference
            parent_path = path_levels[indent_level - 1]

        # Construct the current path
        current_path = os.path.join(parent_path, name)

        # Create directory or file
        if is_dir:
            os.makedirs(current_path, exist_ok=True)
        else:
            open(current_path, "a").close()

        # Update the path_levels dictionary for the current indent level
        path_levels[indent_level] = current_path
        # Clean up any outdated entries in path_levels
        keys_to_remove = [k for k in path_levels if k > indent_level]
        for key in keys_to_remove:
            del path_levels[key]

        # Update last_indent_level for comparison in the next iteration
        last_indent_level = indent_level



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
