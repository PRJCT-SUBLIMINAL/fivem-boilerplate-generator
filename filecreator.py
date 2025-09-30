import os

def generate_files_nui(resource_path):
    html_path = f'{resource_path}/html'
    indexHTML = os.path.join(html_path, "index.html")
    styleCSS = os.path.join(html_path, "style.css")
    scriptJS = os.path.join(html_path, "script.js")

    with open(indexHTML, "w") as f:
        f.write("<!DOCTYPE html>\n<hmtl>\n    <head>\n        <link rel='stylesheet' href='style.css'>\n        <script src='script.js' defer></script>\n    </head>\n    <body>\n    </body>\n<hmtl>")

def generate_files(resource_path):
    print('gen files')
    
def generate_manifest(resource_path, isUiNeeded):
    fxmanifest = os.path.join(resource_path, "fxmanifest.lua")

    if isUiNeeded in ("N", "n"):
        with open(fxmanifest, "w") as f:
            f.write("fx_version 'cerulean' \ngame 'gta5' \nlua54 'yes' \n\nclient_file 'client.lua' \n\nserver_file 'server.lua'")
    elif isUiNeeded in ("Y", "y"):
        with open(fxmanifest, "w") as f:
            f.write("fx_version 'cerulean' \ngame 'gta5' \nlua54 'yes' \n\nclient_file 'client.lua' \n\nserver_file 'server.lua' \n\nui_page 'html/index.html' \n\nfiles {\n    'html/index.hmtl',\n    'html/style.css',\n    'html/script.js'\n}")

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