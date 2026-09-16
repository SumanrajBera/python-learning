import os
from pathlib import Path


def create_folder():
    try:
        folderName = input("Enter folder name: ")
        folderPath = Path(__file__).parent
        lt = list(folderPath.iterdir())

        folders = [item for item in lt if item.is_dir()]
        folderNames = [folder.name for folder in folders]

        if folderName in folderNames:
            print("Folder with such name already exists.\n")
        else:
            (folderPath / folderName).mkdir()
            print("Folder created successfully. \n")

    except Exception as err:
        print("Error occured:", err)


def list_folders():
    try:
        folderPath = Path(__file__).parent
        lt = list(folderPath.iterdir())

        folders = [item for item in lt if item.is_dir()]

        if len(folders) == 0:
            print("There are no folders.\n")
        else:
            for i, fold in enumerate(folders):
                print(f"{i + 1}: {fold.name}")
            print("")
    except Exception as err:
        print("Error occured:", err)


def rename_folder():
    try:
        folderName = input("Enter folder name which you want to rename: ")
        folderPath = Path(__file__).parent
        path = folderPath / folderName

        if not path.exists():
            print("Folder with such name doesn't exists.\n")
        else:
            newName = input("Enter new name for the folder: ")
            path.rename(folderPath / newName)
            print("Folder renamed successfully.\n")
    except Exception as err:
        print("Error occured:", err)


def delete_folder():
    try:
        folderName = input("Enter folder name which you want to delete: ")
        folderPath = Path(__file__).parent
        path = folderPath / folderName

        if not path.exists():
            print("Folder with such name doesn't exists.\n")
        else:
            path.rmdir()
            print("Folder deleted successfully.\n")
    except Exception as err:
        print("Error occured:", err)


def create_file():
    try:
        fileName = input("Enter file name you want to create with extension: ")
        path = Path(__file__).parent

        lt = list(path.glob("*"))
        files = [file.name for file in lt if file.is_file()]

        if fileName in files:
            print("File already exists.\n")
        else:
            with open(f"{path}/{fileName}", "x") as fs:
                print("File created successfully.\n")
    except Exception as err:
        print("Error occured:", err)


def list_files():
    try:
        path = Path(__file__).parent

        lt = list(path.glob("*"))
        files = [file.name for file in lt if file.is_file()]

        if len(files) == 0:
            print("There are no files.\n")
        else:
            for i, file in enumerate(files):
                print(f"{i + 1}: {file}")
            print("")
    except Exception as err:
        print("Error occured:", err)


def rename_file():
    try:
        fileName = input("Enter file name you want to change with extension: ")
        path = Path(__file__).parent

        lt = list(path.glob("*"))
        files = [file.name for file in lt if file.is_file()]

        if fileName == "main.py":
            print("You don't have permission to change this file.\n")
        elif fileName not in files:
            print("File doesn't exists.\n")
        else:
            newFileName = input("Enter new file name with extension: ")
            (path / fileName).rename((path / newFileName))
            print("File name changes successfully.\n")
    except Exception as err:
        print("Error occured:", err)


def delete_file():
    try:
        fileName = input("Enter file name you want to change with extension: ")
        path = Path(__file__).parent

        lt = list(path.glob("*"))
        files = [file.name for file in lt if file.is_file()]

        if fileName not in files:
            print("File doesn't exists.\n")
        else:
            (path / fileName).unlink()
            print("File deleted successfully.\n")
    except Exception as err:
        print("Error occured:", err)


def operate_file():
    print("Choose Options to perform the following operations:")
    print("a: Read from file")
    print("b: Append in file")
    print("c: Overwrite in file")
    option = input("Please enter your option: ")

    try:
        if option != "a" and option != "b" and option != "c":
            raise (Exception("Didn't Enter a valid choice. Please try later!\n"))

        fileName = input("Enter file name you want to change with extension: ")
        path = Path(__file__).parent

        lt = list(path.glob("*"))
        files = [file.name for file in lt if file.is_file()]

        if fileName not in files:
            print("File doesn't exists.\n")
            return

        if option == "a":
            print("Content: ")
            with open(path / fileName) as fs:
                for line in fs.readlines():
                    print(line)
            print()
        elif option == "b":
            if fileName == "main.py":
                print("You don't have permission to operate on this file. \n")
            else:
                with open(path / fileName, "a") as fs:
                    str = input("Enter content that you want to append: ")
                    fs.write(str)
                print()
        elif option == "c":
            if fileName == "main.py":
                print("You don't have permission to operate on this file. \n")
            else:
                with open(path / fileName, "w") as fs:
                    str = input("Enter content that you want to append: ")
                    fs.write("\n" + str)
                print()
    except Exception as err:
        print("Error occured:", err)


while True:
    print("Choose Options to perform the following operations:")
    print("1: Create a Folder")
    print("2: List all Folders")
    print("3: Rename a Folder")
    print("4: Delete a Folder")
    print("5: Create a File")
    print("6: List all Files")
    print("7: Rename a File")
    print("8: Delete a File")
    print("9: Operate on a File")
    print("0: To exit file manager")

    try:
        choice = int(input("Please enter your choice: "))

        if choice == 0:
            break
        elif choice == 1:
            create_folder()
        elif choice == 2:
            list_folders()
        elif choice == 3:
            rename_folder()
        elif choice == 4:
            delete_folder()
        elif choice == 5:
            create_file()
        elif choice == 6:
            list_files()
        elif choice == 7:
            rename_file()
        elif choice == 8:
            delete_file()
        elif choice == 9:
            operate_file()
        else:
            raise (Exception("The choice must be between 0-9"))
    except Exception as err:
        print("Error occured:", err)
