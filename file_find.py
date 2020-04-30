'''
#! python3

file_find.py - Get user input asking for a directory, ask the file extensions
they want to find.  Ask if they want to rename, ask what characters they want
to change.
'''

import os
import shutil


def main():
    '''
    New folder must not exist. File extensions must be preceeded by a period
    and seperated by blank space, for example: " .jpeg .png .gif "
    '''
    # Ask the user to provide the required information.
    root_dir = input("Please enter the path of your root folder: \n")
    new_dir_name = input(
        "Please input a name for the new folder you'd like to create: \n")
    file_extensions_input = input(
        'Please list the file extensions you want to search for or \
            choose a type of file from the options below: \n')
    user_ask_rename = input(
        "Would you like to replace any characters in your filenames? y/n \n")

    # Make a new directory inside the chosen directory to store files.

    # Make a new path to the directory.
    new_dirpath = os.path.join(root_dir, new_dir_name)
    # If the directory doesn't exist, create it.
    if not os.path.exists(new_dirpath):
        os.mkdir(new_dirpath)

    # Get a list of directories, files in the root directory.

    file_list = []
    for (dirname, _, filenames) in os.walk(root_dir):
        # Use a list comprehension.
        file_list += [os.path.join(dirname, filename)
                      for filename in filenames]

    # For files in file tree of root directory, find files with required extension.
    file_extensions = list(file_extensions_input.split())

    for extension in file_extensions:
        for filename in file_list:
            if filename.lower().endswith(extension):
                source_path = os.path.abspath(filename)
                shutil.copy(source_path, new_dirpath)

    # Rename those files if necessary, store them in the new directory.
    if user_ask_rename.lower() == 'y':

        old_char = input('What character would you like to replace? \n')
        new_char = input(
            f'What character would you like to replace {old_char} with? \n')

        for filename in os.listdir(new_dirpath):
            # Find the filepath of the file.
            filepath = os.path.join(new_dirpath, filename)
            # For each file in the new directory, make a new filename.
            replacement_filename = str(os.path.splitext(filename)[
                0]).replace(f'{old_char}', f'{new_char}')
            # Create a new filename, and create a path to that new filename.
            new_filename = replacement_filename + os.path.splitext(filename)[1]
            new_filepath = os.path.join(new_dirpath, new_filename)
            # Rename file.
            os.rename(filepath, new_filepath)

    else:
        pass


if __name__ == '__main__':
    main()
