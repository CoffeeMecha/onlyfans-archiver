#
#
#  _____       _      ______                _____                                  _             _____        __  __         ___  ___          _
# |  _  |     | |     |  ___|              /  ___|                                | |           /  __ \      / _|/ _|        |  \/  |         | |
# | | | |_ __ | |_   _| |_ __ _ _ __  ___  \ `--.  ___ _ __ __ _ _ __   ___ _ __  | |__  _   _  | /  \/ ___ | |_| |_ ___  ___| .  . | ___  ___| |__   __ _
# | | | | '_ \| | | | |  _/ _` | '_ \/ __|  `--. \/ __| '__/ _` | '_ \ / _ \ '__| | '_ \| | | | | |    / _ \|  _|  _/ _ \/ _ \ |\/| |/ _ \/ __| '_ \ / _` |
# \ \_/ / | | | | |_| | || (_| | | | \__ \ /\__/ / (__| | | (_| | |_) |  __/ |    | |_) | |_| | | \__/\ (_) | | | ||  __/  __/ |  | |  __/ (__| | | | (_| |
#  \___/|_| |_|_|\__, \_| \__,_|_| |_|___/ \____/ \___|_|  \__,_| .__/ \___|_|    |_.__/ \__, |  \____/\___/|_| |_| \___|\___\_|  |_/\___|\___|_| |_|\__,_|
#                 __/ |                                         | |                       __/ |
#                |___/                                          |_|                      |___/
#
#
#    _     _   _                  _____            _ _   _                                  __                   _                         __  __
#                                                        ____  ________    _________   _____ ___________    ____  _   __
#                                                       / __ \/ ____/ /   / ____/   | / ___// ____/ ___/   / __ \/ | / /
#                                                      / /_/ / __/ / /   / __/ / /| | \__ \/ __/  \__ \   / / / /  |/ /
#                                                     / _, _/ /___/ /___/ /___/ ___ |___/ / /___ ___/ /  / /_/ / /|  /
#                                                    /_/ |_/_____/_____/_____/_/  |_/____/_____//____/   \____/_/ |_/
#
#
#
#
#  | |__ | |_| |_ _ __  ___ _   / / / |___      _(_) |_| |_ ___ _ __ ___ ___  _ __ ___    / / __ ___   ___  ___| |__   __ _     ___ ___  / _|/ _| ___  ___
#  | '_ \| __| __| '_ \/ __(_) / / /| __\ \ /\ / / | __| __/ _ \ '__/ __/ _ \| '_ ` _ \  / / '_ ` _ \ / _ \/ __| '_ \ / _` |   / __/ _ \| |_| |_ / _ \/ _ \
#  | | | | |_| |_| |_) \__ \_ / / / | |_ \ V  V /| | |_| ||  __/ |_| (_| (_) | | | | | |/ /| | | | | |  __/ (__| | | | (_| |  | (_| (_) |  _|  _|  __/  __/
#  |_| |_|\__|\__| .__/|___(_)_/_/   \__| \_/\_/ |_|\__|\__\___|_(_)\___\___/|_| |_| |_/_/ |_| |_| |_|\___|\___|_| |_|\__,_|___\___\___/|_| |_|  \___|\___|
#                |_|                                                                                                      |_____|
#
#                                                                    https://twitter.com/mecha_coffee
#                                                             https://github.com/CoffeeMecha/onlyfans-archiver
#
#

import ctypes
import json
import os
import time
import tkinter as tk
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from tkinter import *
from tkinter import ttk
from urllib.parse import urlparse

import requests
import webbrowser

executor = ThreadPoolExecutor(max_workers=10)


def terminate_thread(thread):
    """Terminates a python thread from another thread.

    :param thread: a threading.Thread instance
    """
    if not thread.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


# this is a function to get the user input from the text input box
def getUsernameInputBoxValue():
    userInput = usernameInput.get()
    return userInput


def redirector(inputStr):
    terminal.insert(INSERT, inputStr)
    terminal.see(tk.END)


sys.stdout.write = redirector


# this is a function to get the user input from the text input box
def getAccessInputBoxValue():
    userInput = accessInput.get()
    return userInput


# this is a function to get the user input from the text input box
def getUAInputBoxValue():
    userInput = useragentInput.get()
    return userInput


def startFarting():
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
        print("downloads Folder Did Not Exist, Created!")
    file_path = f"downloads/{getUsernameInputBoxValue()}"
    if not os.path.exists(f"downloads/{getUsernameInputBoxValue()}"):
        os.makedirs(f"downloads/{getUsernameInputBoxValue()}")
        print(
            f"{getUsernameInputBoxValue()} Folder Did Not Exist in downloads Folder, Created!"
        )
    # userName = input('Enter username:')
    # accessToken = input('Enter access-token:')
    # userAgent = input('Enter User-Agent:')
    url = f"https://onlyfans.com/api2/v2/users/{getUsernameInputBoxValue()}?app-token=33d57ade8c02dbc5a333db99ff9ae26a"
    headers = {"accept": "application/json, text/plain, */*"}
    response = requests.request("GET", url, headers=headers)
    print(f"Got User ID: {response.json()['id']}")
    url = f"https://onlyfans.com/api2/v2/users/{response.json()['id']}/posts?limit=100&order=publish_date_desc&skip_users=all&skip_users_dups=1&pinned=0&app-token=33d57ade8c02dbc5a333db99ff9ae26a"
    headers = {
        "accept": "application/json, text/plain, */*",
        "access-token": getAccessInputBoxValue(),
        "user-agent": getUAInputBoxValue(),
    }

    response = requests.request("GET", url, headers=headers)

    for data in response.json():
        print(f"Post ID: {data['id']}")
        for media in data["media"]:
            # print(f"Photo URL: {media['source']['source']}")
            a = urlparse(media["source"]["source"])
            if media["source"]["source"] == None:
                pass
            else:
                fileName = os.path.basename(a.path)
                fileNameWithPath = f"{file_path}/{fileName}"
                url = media["source"]["source"]
                print(f"Downloading {fileName}")
                executor.submit(download, fileName, fileNameWithPath, url)
                print(f"Downloaded {fileName}")


def download(fileName, fileNameWithPath, url):
    print(f"Downloading {fileName}")
    urllib.request.urlretrieve(url, fileNameWithPath)
    return "File Downloaded"


def linkCallback(url):
    webbrowser.open_new(url)


# this is the function called when the button is clicked
def mfClicked():
    Label(
        root, text="Started, check output!", bg="#F0F8FF", font=("arial", 12, "normal")
    ).place(x=25, y=256)
    executor.submit(startFarting)


def abortClicked():
    executor.shutdown(wait=False)
    for t in executor._threads:
        terminate_thread(t)
        print(
            "All threads killed, safe to close the window! Please re-run the script if you want to download again!"
        )
        Label(
            root,
            text="Stopped!                              ",
            bg="#F0F8FF",
            font=("arial", 12, "normal"),
        ).place(x=25, y=256)


root = Tk()

# This is the section of code which creates the main window
root.geometry("950x550")
root.configure(background="#F0F8FF")
root.title("OnlyFans Scraper")


# This is the section of code which creates the a label
Label(root, text="Enter Username", bg="#F0F8FF", font=("arial", 12, "normal")).place(
    x=25, y=36
)

gitLink = Label(
    root,
    text="https://github.com/CoffeeMecha/onlyfans-archiver",
    bg="#F0F8FF",
    fg="blue",
    cursor="hand2",
    font=("arial", 12, "normal"),
)
gitLink.pack()
gitLink.bind(
    "<Button-1>",
    lambda e: linkCallback("https://github.com/CoffeeMecha/onlyfans-archiver"),
)
gitLink.place(x=270, y=36)


# This is the section of code which creates the a label
Label(
    root, text="Enter access-token", bg="#F0F8FF", font=("arial", 12, "normal")
).place(x=25, y=96)


# This is the section of code which creates the a label
Label(root, text="Enter User-Agent", bg="#F0F8FF", font=("arial", 12, "normal")).place(
    x=25, y=156
)


# This is the section of code which creates a text input box
usernameInput = Entry(root)
usernameInput.place(x=25, y=56)


# This is the section of code which creates a text input box
accessInput = Entry(root)
accessInput.place(x=25, y=116)


# This is the section of code which creates a text input box
useragentInput = Entry(root)
useragentInput.place(x=25, y=176)


# This is the section of code which creates a button
Button(
    root, text="GO!!!", bg="#46de00", font=("arial", 12, "normal"), command=mfClicked
).place(x=25, y=216)

# This is the section of code which creates a button
Button(
    root,
    text="ABORT!!!",
    bg="#FF1100",
    font=("arial", 12, "normal"),
    command=abortClicked,
).place(x=85, y=216)


# This is the section of code which creates the a label
Label(root, text="Waiting to start!", bg="#F0F8FF", font=("arial", 12, "normal")).place(
    x=25, y=256
)


# This is the section of code which creates a text input box
terminal = tk.Text(root)
terminal.place(x=265, y=56)


root.mainloop()
