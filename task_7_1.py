import os

new_project = 'my_project'
if not os.path.exists(new_project):
    os.mkdir(new_project)

def add_folder(folder_name):
    new_folder = os.path.join('my_project', folder_name)
    if not os.path.exists(new_folder):
         os.makedirs(new_folder)

add_folder('settings')
add_folder('mainapp')
add_folder('adminapp')
add_folder('authapp')
