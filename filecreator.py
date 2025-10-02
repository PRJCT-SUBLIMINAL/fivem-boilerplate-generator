import os
import shutil

def generate_files_nui(resource_path):
    html_path = f'{resource_path}/html'
    indexHTML = os.path.join(html_path, "index.html")
    styleCSS = os.path.join(html_path, "style.css")
    scriptJS = os.path.join(html_path, "script.js")

    shutil.copyfile('bin/index.html', f'{indexHTML}')
    shutil.copyfile('bin/style.css', f'{styleCSS}')
    shutil.copyfile('bin/script.js', f'{scriptJS}')

#    with open(indexHTML, "w") as f:
#        f.write("<!DOCTYPE html>\n<hmtl>\n    <head>\n        <link rel='stylesheet' href='style.css'>\n        <script src='script.js' defer></script>\n    </head>\n    <body>\n    </body>\n<hmtl>")
#    with open(styleCSS, "w") as f:
#        f.write("body {\n  margin: 0px;\n}")
#    with open(scriptJS, "w") as f:
#        f.write("console.log('script.js loaded')")

def generate_files(resource_path):
    client_path = f'{resource_path}/client'
    server_path = f'{resource_path}/server'

    clientLua = os.path.join(client_path, "cl_main.lua")
    serverLua = os.path.join(server_path, "sv_main.lua")
    configLua = os.path.join(resource_path, "config.lua")

    shutil.copyfile('bin/cl_main.lua', f'{clientLua}')
    shutil.copyfile('bin/sv_main.lua', f'{serverLua}')
    shutil.copyfile('bin/config.lua', f'{configLua}')

#    with open(clientLua, "w") as f:
#        f.write("--local QBCore = exports['qb-core]:GetCoreObject()\nlocal function debug(text)\n    if Config.Debug == false then return end\n    print('[DEBUG] '..text)\nend")

#    with open(serverLua, "w") as f:
#        f.write("--local QBCore = exports['qb-core]:GetCoreObject()\nlocal function debug(text)\n    if Config.Debug == false then return end\n    print('[DEBUG] '..text)\nend")
    
#    with open(configLua, "w") as f:
#        f.write("Config = { }\nConfig.Debug = true")

def generate_manifest(resource_path, isUiNeeded):
    fxmanifest = os.path.join(resource_path, "fxmanifest.lua")

    if isUiNeeded in ("N", "n"):
        with open(fxmanifest, "w") as f:
            f.write("fx_version 'cerulean' \ngame 'gta5' \nlua54 'yes' \n\nshared_files {'config.lua'} \n\nserver_file 'server/sv_main.lua' \n\nclient_file 'client/cl_main.lua'")
    elif isUiNeeded in ("Y", "y"):
        with open(fxmanifest, "w") as f:
            f.write("fx_version 'cerulean' \ngame 'gta5' \nlua54 'yes' \n\nshared_files {'config.lua'} \n\nserver_files {'server/sv_main.lua'} \n\nclient_files {'client/cl_main.lua'} \n\nui_page 'html/index.html' \n\nfiles {\n    'html/index.hmtl',\n    'html/style.css',\n    'html/script.js'\n}")

def generate_folders(formatted_pathstring, isUiNeeded):
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
    
    generate_manifest(resource_path, isUiNeeded)

def initialize_resource():
    resource_name = input('Please enter the name for your resource: ')
    isUiNeeded = input('Do you want to use NUI? Please input Y/N: ')

    formatted_pathstring = resource_name.lower()

    generate_folders(formatted_pathstring, isUiNeeded)