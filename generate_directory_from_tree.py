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
    path_levels = {0: base_path}  # Initialize the root path
    last_indent_level = 0  # Keep track of the last line's indent level

    for line in tree.strip().split('\n'):
        indent_count = 0
        cleaned_line = line.lstrip("|")

        for char in cleaned_line:
            if char in [' ', '+', '-']:
                indent_count += 1
            elif char.isalnum():
                break

        indent_level = indent_count // 2
        name = line.strip(' |+-')
        is_dir = '+' in line

        # Handling the hierarchical structure based on indent_level comparison
        if indent_level > last_indent_level:
            # If current indent level is greater, make this line the child of the one before it
            current_path = os.path.join(path_levels[last_indent_level], name)
        elif indent_level == last_indent_level:
            # If indent level is the same, sibling case
            current_path = os.path.join(os.path.dirname(path_levels[last_indent_level]), name)
        else:
            # If current indent level is smaller, go up the hierarchy as needed
            # Determine how many levels to go up
            level_difference = last_indent_level - indent_level
            while level_difference > 0:
                current_path = os.path.dirname(path_levels[last_indent_level - level_difference])
                level_difference -= 1
            current_path = os.path.join(current_path, name)

        # Update or create the directory/file based on is_dir
        if is_dir:
            os.makedirs(current_path, exist_ok=True)
        else:
            open(current_path, "a").close()

        # Update path_levels for the current indent level and clean up higher levels
        path_levels[indent_level] = current_path
        for key in list(path_levels.keys()):
            if key > indent_level:
                del path_levels[key]

        # Update last_indent_level for the next iteration
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
