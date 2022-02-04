import os
import shutil


def make_file(file_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        if os.path.exists(file_name):
            print('FILE EXIST!')
        else:
            with open(file_name, 'a') as file:
                print('FILE CREATED')
    except FileNotFoundError:
        print('INCORRECT INPUT')


def remove_file(file_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        os.remove(file_name)
        print('FILE REMOVED')
    except FileNotFoundError:
        print('FILE NOT FOUND')


def file_viewer(file_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for i in file.readlines():
                print(i, end='')
    except FileNotFoundError:
        print("FILE NOT FOUND")


def file_writer(file_name):
    try:
        with open(file_name, 'a') as file:
            file.writelines(input('INPUT TEXT FOR WRITING: \n') + '\n')
            os.system('cls' if os.name == 'nt' else 'clear')
        print('WRITE INTO FILE')
    except FileNotFoundError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('INCORRECT INPUT')


def rename_file(file_name, new_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        os.rename(file_name, new_name)
        print('FILE`S RENAMED')
    except FileNotFoundError:
        print('FILE NOT FOUND!')


def copy_file(file_name, new_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        shutil.copy2(file_name, new_name)
        print('FILE`S COPIED')
    except shutil.SameFileError:
        print('DIST IS THE SAME FILENAME')
    except FileNotFoundError:
        print('FILE NOT FOUND')
    except PermissionError:
        print('PERMISSION DENIED')
    except FileExistsError:
        print('FILE EXISTS')



def move_file(file_name, dist_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        shutil.move(file_name, dist_name)
        print('FILE`S MOVED')
    except shutil.SameFileError:
        print('DIST IS THE SAME FILENAME')
    except FileNotFoundError:
        print('FILE NOT FOUND')
    except PermissionError:
        print('PERMISSION DENIED')
    except FileExistsError:
        print('FILE EXISTS')