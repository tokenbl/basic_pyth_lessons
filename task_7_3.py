import os, shutil


def copy_folder(root_dir, dest_dir):
    for src_dir, dirs, files in os.walk(root_dir):
        n_dir = src_dir.replace(root_dir, dest_dir, 1)
        if not os.path.exists(n_dir):
            os.makedirs(n_dir)
        for file_ in files:
            root_file = os.path.join(src_dir, file_)
            dest_file = os.path.join(n_dir, file_)
            if os.path.exists(dest_file):
                os.remove(dest_file)
            shutil.copy(root_file, n_dir)

copy_folder(r'C:\Users\Администратор\PycharmProjects\pythonProject\my_project\authapp\templates',
            r'C:\Users\Администратор\PycharmProjects\pythonProject\my_project\templates')
copy_folder(r'C:\Users\Администратор\PycharmProjects\pythonProject\my_project\mainapp\templates',
            r'C:\Users\Администратор\PycharmProjects\pythonProject\my_project\templates')
