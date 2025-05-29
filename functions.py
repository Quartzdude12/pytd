# functions

import os
import sys
import keyboard
import tinydb

def mktsk():
    tskname = str(input("Enter task name: "))
    return task(tskname, False)

def mklist():
    listname = str(input("Enter list name:"))
    return tdlist([], listname)

def cleer():
    os.system('cls' if os.name == 'nt' else 'clear')

def printvers(): #boilerplate :/
    print("Python version: ", sys.version.split()[0])
    print("TinyDB version: ", tinydb.__version__)
    print("Keyboard version: ", keyboard.version)
    print("pyTD version: -1")

