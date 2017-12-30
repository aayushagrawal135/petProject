import webbrowser
import lazy
import requests

def open(shortcut):
   try:
       list = lazy.suggestion_list(shortcut)
       if len(list) == 0:
           print("No such keyword present to rename")
       elif len(list) == 1:
           url = lazy.read_url(str(shortcut))
           url = url[0][0]
           webbrowser.open(url)
       else:
           for x in range(len(list)):
               print(list[x])
   except:
       print("Shortcut doesn't exist")


def add_custom_shortcut(shortcut, url):
    try:
        request = requests.get(url)
        if request.status_code == 200:
            lazy.data_entry(shortcut, url)
    except:
        print("Fishy, try again")

def see_existing_shortcuts():
    lazy.see_existing_shortcuts()

def rename_shortcut(old, new):
    list = lazy.suggestion_list(old)
    if len(list)== 0:
        print("No such keyword present to rename")
    elif len(list) == 1:
        lazy.rename_shortcut(old, new)
    else:
        for x in range(len(list)):
            print(list[x])

def delete(name):
    list = lazy.suggestion_list(name)
    if len(list) == 0:
        print("No such keyword present to delete")
    elif len(list) == 1:
        lazy.delete(name)
    else:
        for x in range(len(list)):
            print(list[x])

def help():
    list = ["add", "help", "open", "rename", "see"]
    for x in range(len(list)):
        print(list[x])

def do(args):
    if len(args) > 1:
        command = str(args[1])

        if command == "open" and len(args) == 3:
            name = args[2]
            open(name)

        elif command == "add" and len(args) == 4:
            name = args[2]
            url = args[3]
            add_custom_shortcut(name, url)

        elif command == "rename" and len(args) == 4:
            old = args[2]
            new = args[3]
            rename_shortcut(old, new)

        elif command == "see" and len(args) == 2:
            see_existing_shortcuts()

        elif command == "help" and len(args) == 2:
            help()

        elif command == "del" and len(args) == 3:
            name = args[2]
            delete(name)

        lazy.close()

    else:
        print("Enter command type - help")

