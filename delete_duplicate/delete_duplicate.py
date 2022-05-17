from os import listdir, remove
from os.path import isfile, join, exists
import filecmp


def delete_duplicate_files(my_path: str) -> list:
    files = [join(my_path, f)
             for f in listdir(my_path) if isfile(join(my_path, f))]
    files_to_delete = []
    for i in range(len(files)):
        for j in range(i+1, len(files)):
            if filecmp.cmp(files[i], files[j]):
                files_to_delete.append([files[i], files[j]])

    delete_files_in_list(files_to_delete)


def delete_files_in_list(files):
    if len(files) == 0:
        print("No files to delete")
    for file1, file2 in files:
        if exists(file1) and exists(file2):
            print(f"Deleting {file1}...")
            remove(file1)


if __name__ == "__main__":
    delete_duplicate_files("./")
