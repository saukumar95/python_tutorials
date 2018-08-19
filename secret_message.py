import os
import re


def rename_files():
    # (1) Get file names from the computer folder
    file_list = os.listdir("/home/banti/Desktop/prank")

# (2) Renaming the file in that folder
    for file_name in file_list:
        os.renames(file_name, re.sub('[0-9]', '', file_name)
rename_files()