import os
import os.path
import filecmp


def delete_duplicate_files(my_path: str) -> list:
    files = [os.path.join(my_path, f)
             for f in os.listdir(my_path) if os.path.isfile(os.path.join(my_path, f))]
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
        if os.path.exists(file1) and os.path.exists(file2):
            print(f"Deleting {file1}...")
            os.remove(file1)


if __name__ == "__main__":
    delete_duplicate_files("./")
