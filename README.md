# Directory Structure Generator

## Overview

This Python script generates a directory structure based on a tree defined in a text file. It features a simple graphical user interface (GUI) that allows users to specify the input file containing the directory tree, the root directory name, and the custom path where the directory structure will be created.
This can either be used in conjunction with my other project https://github.com/ALEKSJZU/generate-directory-tree, where you use it to generate a txt file containing the string representation of an existing directory and modify in that txt file for this project to read from,
or you may use chatbots such as ChatGPT to generate the file structure in the format listed in the example below.
## Dependencies

- Python 3.x
- Tkinter (should be included with Python)

## Setup

No additional setup is required if you're running a standard Python installation, as Tkinter is included with Python by default.

## How to Use

1. **Start the Script**: Run the script from your terminal or command prompt.

```bash
python generate_directory_from_tree.py
```
1. Select the Directory Tree File: A file dialog will open. Navigate to and select the .txt file that contains your directory structure.

2. Enter the Root Directory Name: A prompt will appear asking you to enter the name of the root directory for your project.

3. Choose the Custom Path: A directory selection dialog will open for you to choose where the directory structure should be created in your filesystem.

4. Completion: After selecting the necessary inputs, the script will generate the directory structure. A success message will appear once the process is completed.


## File Format
### The directory tree should be defined in a text file with the following format:

1. Use + at the beginning of a line for directories.
2. Use - at the beginning of a line for files.
3. Indentation (using spaces) determines the hierarchy.

### Example:
```
+ project-root
  + backend
    + models
      - user.js
    - server.js
  + frontend
    - index.html
```
## Contributing
Feel free to fork this repository and submit pull requests to contribute to the development of this script. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT
