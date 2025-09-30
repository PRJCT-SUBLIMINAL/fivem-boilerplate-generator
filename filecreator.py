import os

def generate_files_nui(resource_path):
    print('nui')

def generate_files(resource_path):
    print('gen files')
    
def generate_manifest(resource_path, isUiNeeded):
    fxmanifest = os.path.join(resource_path, "fxmanifest.lua")

    if isUiNeeded in ("N", "n"):
        with open(fxmanifest, "w") as f:
            f.write("fx_version 'cerulean' \ngame 'gta5' \nlua54 'yes' \n\nclient_file 'client.lua' \n\nserver_file 'server.lua'")

def generate_folders(formatted_pathstring, isUiNeeded):
    resource_path = f'output/{formatted_pathstring}'
    os.makedirs(resource_path, exist_ok=True)
    os.mkdir(f'{resource_path}/client')
    os.mkdir(f'{resource_path}/server')

    if isUiNeeded in ("Y", "y"):
        print('NUI needed. Creating "html" folder')
        os.mkdir(f'{resource_path}/html')
        generate_files_nui(resource_path)
        generate_files(resource_path)
    elif isUiNeeded in ("N", "n"):
        generate_files(resource_path)
        print('NUI not needed.')
    
    generate_manifest(resource_path, isUiNeeded)

def initialize_resource():
    resource_name = input('Please enter the name for your resource: ')
    isUiNeeded = input('Do you want to use NUI? Please input Y/N: ')

    formatted_pathstring = resource_name.lower()

    generate_folders(formatted_pathstring, isUiNeeded)