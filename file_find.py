'''
#! Python3

file_find.py - Get user input asking for a directory, ask the file extensions
they want to find.  Ask if they want to rename, ask what characters they want
to change.
'''

import os
import shutil
from extension_dict import EXTENSION_DICT


def main():
    '''
    New folder must not exist. File extensions must be preceeded by a period
    and seperated by blank space, for example: " .jpeg .png .gif "
    '''
    extensions = list(EXTENSION_DICT.keys())
    extension_list = [extensions[i] for i in range(len(extensions))]

    # Ask the user to provide the required information.
    root_dir = input("Please enter the path of your root folder: \n")
    new_dir_name = input(
        "Please input a name for the new folder you'd like to create: \n")
    file_extensions_input = input(
        f'Please list the file extensions you want to search for or choose a type of file from the options below:\n{", ".join(extension_list)}\n')
    user_ask_rename = input(
        "Would you like to replace any characters in your filenames? y/n \n")

    new_dirpath = os.path.join(root_dir, new_dir_name)
    if not os.path.exists(new_dirpath):
        os.mkdir(new_dirpath)
    # Generate a list of files to copy.
    file_list = []
    for (dirname, _, filenames) in os.walk(root_dir):
        file_list += [os.path.join(dirname, filename)
                      for filename in filenames]

    # Handle user inputs, either an option in EXTENSION_DICT or user list.
    if file_extensions_input not in extension_list:
        file_extensions = list(file_extensions_input.split())

    else:
        for i in range(len(extension_list)):
            if file_extensions_input == extension_list[i]:
                file_extensions = list(EXTENSION_DICT[f'{extension_list[i]}'])

    for extension in file_extensions:
        for filename in file_list:
            if filename.lower().endswith(extension):
                source_path = os.path.abspath(filename)
                shutil.copy(source_path, new_dirpath)

    # Rename files option
    if user_ask_rename.lower() == 'y':

        old_char = input('What character would you like to replace? \n')
        new_char = input(
            f'What character would you like to replace {old_char} with? \n')
        # Rename file within the new directory only.
        for filename in os.listdir(new_dirpath):

            filepath = os.path.join(new_dirpath, filename)

            replacement_filename = str(os.path.splitext(filename)[
                0]).replace(f'{old_char}', f'{new_char}')

            new_filename = replacement_filename + os.path.splitext(filename)[1]
            new_filepath = os.path.join(new_dirpath, new_filename)
            os.rename(filepath, new_filepath)

    else:
        pass


if __name__ == '__main__':
    main()
