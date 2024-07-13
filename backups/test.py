#!/usr/bin/python3

import os

def get_files_sorted_by_name(directory):
    # Get all file names in the directory
    files = [file for file in os.listdir(directory) if file.startswith("web_static_") and file.endswith(".tgz")]

    # Sort files based on their names
    sorted_files = sorted(files)

    return sorted_files

# Example usage
directory = "/home/assimine/Documents/ALX/Code/AirBnB_clone_v2/versions"
sorted_files = get_files_sorted_by_name(directory)

for file in sorted_files:
    print(file)
