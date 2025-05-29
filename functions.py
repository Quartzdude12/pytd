# functions

import os
import sys
import keyboard
import tinydb
from task import *

def mktsk():
    tskname = str(input("Enter task name: "))
    return task(tskname, False)

def mklist():
    listname = str(input("Enter list name:"))
    return tdlist([], listname)

def cleer():
    os.system('cls' if os.name == 'nt' else 'clear')

def select_list():
    pass
