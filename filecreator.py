import os
import shutil
import sys
import time

RESOURCE_NAME = ' # FiveM Resource Generator 2.3 # '
print('__________________________')
print('')
print(f'{RESOURCE_NAME}')
print('__________________________')
print('')

def generate_files_nui(resource_path):
    print(' Generating NUI files... ')
    html_path = f'{resource_path}/html'
    indexHTML = os.path.join(html_path, "index.html")
    styleCSS = os.path.join(html_path, "style.css")
    scriptJS = os.path.join(html_path, "script.js")

    shutil.copyfile('bin/index.html', f'{indexHTML}')
    shutil.copyfile('bin/style.css', f'{styleCSS}')
    shutil.copyfile('bin/script.js', f'{scriptJS}')

def generate_files(resource_path):
    print(' Generating Lua files... ')
    client_path = f'{resource_path}/client'
    server_path = f'{resource_path}/server'

    clientLua = os.path.join(client_path, "cl_main.lua")
    serverLua = os.path.join(server_path, "sv_main.lua")
    configLua = os.path.join(resource_path, "config.lua")

    shutil.copyfile('bin/cl_main.lua', f'{clientLua}')
    shutil.copyfile('bin/sv_main.lua', f'{serverLua}')
    shutil.copyfile('bin/config.lua', f'{configLua}')

def generate_manifest(resource_path, isUiNeeded, game):
    print(' Writing fxmanifest.lua... ')
    fxmanifest = os.path.join(resource_path, "fxmanifest.lua")

    if game in 'fivem':
        if isUiNeeded in ("N", "n"):
            print(' NUI generated: No ')
            with open(fxmanifest, "w") as f:
                f.write("fx_version 'cerulean' \ngame 'gta5' \nlua54 'yes' \n\nshared_files {'config.lua'} \n\nserver_file 'server/sv_main.lua' \n\nclient_file 'client/cl_main.lua'")
        elif isUiNeeded in ("Y", "y"):
            print(' NUI generated: Yes ')
            with open(fxmanifest, "w") as f:
                f.write("fx_version 'cerulean' \ngame 'gta5' \nlua54 'yes' \n\nshared_files {'config.lua'} \n\nserver_files {'server/sv_main.lua'} \n\nclient_files {'client/cl_main.lua'} \n\nui_page 'html/index.html' \n\nfiles {\n    'html/index.html',\n    'html/style.css',\n    'html/script.js'\n}")
    elif game in 'redm':
        if isUiNeeded in ("N", "n"):
            print(' NUI generated: No ')
            with open(fxmanifest, "w") as f:
                f.write("fx_version 'cerulean' \ngame 'rdr3' \nlua54 'yes' \n\nshared_files {'config.lua'} \n\nserver_file 'server/sv_main.lua' \n\nclient_file 'client/cl_main.lua'")
        elif isUiNeeded in ("Y", "y"):
            print(' NUI generated: Yes ')
            with open(fxmanifest, "w") as f:
                f.write("fx_version 'cerulean' \ngame 'rdr3' \nlua54 'yes' \n\nshared_files {'config.lua'} \n\nserver_files {'server/sv_main.lua'} \n\nclient_files {'client/cl_main.lua'} \n\nui_page 'html/index.html' \n\nfiles {\n    'html/index.html',\n    'html/style.css',\n    'html/script.js'\n}")


def generate_folders(formatted_pathstring, isUiNeeded, game):
    resource_path = f'output/{formatted_pathstring}'
    os.makedirs(resource_path, exist_ok=True)
    os.mkdir(f'{resource_path}/client')
    os.mkdir(f'{resource_path}/server')

    if isUiNeeded in ("Y", "y"):
        os.mkdir(f'{resource_path}/html')
        generate_files_nui(resource_path)
        generate_files(resource_path)
    elif isUiNeeded in ("N", "n"):
        generate_files(resource_path)
    
    generate_manifest(resource_path, isUiNeeded, game)

    print(f' Resource successfully generated in directory: "/output/{formatted_pathstring}" ')

    time.sleep(1)

    prompt_to_continue()

def prompt_to_continue():
    to_continue = input(' Do you want to continue? Please input Y/N: ')

    if to_continue in ('Y', 'y'):
        initialize_resource()
    elif to_continue in ('N', 'n'):
        sys.exit()

def initialize_resource():
    name_input = input(' Please enter the name for your resource: ')

    if len(name_input) == 0:
        raise Exception(' Resource name can\'t be blank ')
    
    isUiNeeded = input(' Do you want to use NUI? Please input Y/N: ')

    if isUiNeeded not in ('Y', 'y', 'N', 'n'):
        raise Exception(' You need to input Y/N ')
    
    game = input(' Which game do you want to generate this resource for? (FiveM [fivem] / RedM [redm]) Please input "fivem" or "redm" without the quotation marks: ')

    if game not in ('fivem', 'redm'):
        raise Exception(' You need to input "fivem" or "redm"')

    formatted_pathstring = name_input.lower()

    generate_folders(formatted_pathstring, isUiNeeded, game)