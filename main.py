import file_function.file_maker as files
import file_function.dir_maker as dirs
import os
from tkinter import *
import tkinter
from tkinter import ttk
fm = Tk()
fm.title("hallo")
hph = ttk.Frame(fm, padding=10)
hph.grid()
ttk.Label(hph, text="File Manager").grid(column=0, row=0)



# os.system('cls'if os.name == 'nt' else 'clear')


# dirs.dir_viewer()

def filemanager(command):
    
    if command.lower() == '1' or command.lower() == 'move':
        h2=Tk()
        h2h = ttk.Frame(h2, padding=10)
        h2h.grid
        h2.geometry("300x150")
        h2.resizable(False, False)
        h2.title('Pindah File')         
        # command = input('1_FILE OR 2_DIRECTORY:\n')
        
        def  pembagian(bagian):
            pindah = ttk.Frame(h2h)
            pindah.grid
            if bagian.lower() == '1' or command.lower() == 'file' :
                
                file = tk.StringVar()
                folder = tk.StringVar()
                def kirim():
                    files.move_file({file.get()}, {folder.get()})

                # dari
                
                file_label = ttk.Label(pindah, text="Nama File:")
                file_label.pack(fill='x', expand=True)

                file_entry = ttk.Entry(pindah, textvariable=file)
                file_entry.pack(fill='x', expand=True)
                file_entry.focus()
                # ke
                file_label = ttk.Label(pindah, text="Kemana:")
                file_label.pack(fill='x', expand=True)

                file_entry = ttk.Entry(pindah, textvariable=folder)
                file_entry.pack(fill='x', expand=True)
                file_entry.focus()
                # kirim data
                login_button = ttk.Button(signin, text="Login", command=kirim)
                login_button.pack(fill='x', expand=True, pady=10)
                # 
            elif bagian.lower() == '2' or command.lower() == 'folder' :
                dirs.move_dir(input('INPUT SOURCE:\n'), input('INPUT DESTINATION:\n'))
            else:
                print('INCORRECT INPUT')
        Radiobutton(h2h, text="File",command=pembagian('file')).grid(column=1,row=1)
        Radiobutton(h2h, text="Folder",command=pembagian('folder')).grid(column=1,row=1)   
       

#     ##########################  COPY ###################################
    elif command.lower() == '2' or command.lower() == 'copy':
        command = input('1_FILE OR 2_DIRECTORY:\n')
        if command.lower() == '1' or command.lower() == 'file':
            files.copy_file(input('INPUT SOURCE:\n'), input('INPUT DESTINATION:\n'))
        elif command.lower() == '2' or command.lower() == 'directory':
            dirs.copy_dir(input('INPUT SOURCE:\n'), input('INPUT DESTINATION:\n'))
        else:
            print('INCORRECT INPUT')
#     ##########################  RENAME ###################################
#     elif command.lower() == '3' or command.lower() == 'rename':
#         command = input('1_FILE OR 2_DIRECTORY:\n')
#         if command.lower() == '1' or command.lower() == 'file':
#             files.rename_file(input('INPUT OLD NAME:\n'), input('INPUT NEW NAME:\n'))
#         elif command.lower() == '2' or command.lower() == 'directory':
#             dirs.rename_dir(input('INPUT OLD NAME:\n'), input('INPUT NEW NAME:\n'))
#         else:
#             print('INCORRECT INPUT')
#     ##########################  CREATE ###################################
#     elif command.lower() == '4' or command.lower() == 'create':
#         command = input('1_FILE OR 2_DIRECTORY:\n')
#         if command.lower() == '1' or command.lower() == 'file':
#             files.make_file(input('INPUT NAME: \n'))
#         elif command.lower() == '2' or command.lower() == 'directory':
#             dirs.make_dir(input('INPUT NAME: \n'))
#         else:
#             print('INCORRECT INPUT')
#     ##########################  DELETE ###################################
#     elif command.lower() == '5' or command.lower() == 'delete':
#         command = input('1_FILE OR 2_DIRECTORY:\n')
#         if command.lower() == '1' or command.lower() == 'file':
#             files.remove_file(input('INPUT NAME: \n'))
#         elif command.lower() == '2' or command.lower() == 'directory':
#             dirs.remove_dir(input('INPUT NAME: \n'))
#         else:
#             print('INCORRECT INPUT')
#     ##########################  GOTO ###################################
#     elif command.lower() == '6' or command.lower() == 'goto':
#         dirs.dir_change(input('INPUT PATH: \n'))
#     ##########################  VIEW ###################################
#     elif command.lower() == '7' or command.lower() == 'view':
#         files.file_viewer(input('INPUT FILE NAME: \n'))
#     ##########################  EDIT ###################################
#     elif command.lower() == '8' or command.lower() == 'edit':
#         files.file_writer(input('INPUT FILE NAME: \n'))
#     ##########################  EXIT ###################################
#     elif command.lower() == '9' or command.lower() == 'exit':
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print('GOODBYE!')
#         exit()
#     else:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print('INCORRECT COMMAND')
#     print('#' * 100)
#     print('#' * 100)

ttk.Button(hph, text="Move", command= filemanager('move')).grid(column=1, row=1)
ttk.Button(hph, text="Copy", command= filemanager('copy')).grid(column=1, row=0)
# ttk.Button(hph, text="Rename", command=filemanager("3")).grid(column=0, row=2)
# ttk.Button(hph, text="Create", command=filemanager("4")).grid(column=0, row=3)
# ttk.Button(hph, text="Delete", command=filemanager("5")).grid(column=1, row=0)
# ttk.Button(hph, text="Go To", command=filemanager("6")).grid(column=1, row=1)
# ttk.Button(hph, text="View", command=filemanager("7")).grid(column=1, row=2)
# ttk.Button(hph, text="Edit", command=filemanager("8")).grid(column=1, row=3)
# ttk.Button(hph, text="Exit", command=filemanager("9")).grid(column=0, row=2)
##########################  MOVE ###################################
    
fm.mainloop()
