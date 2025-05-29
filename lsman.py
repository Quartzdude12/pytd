import os
import sys
from functions import mktsk, mklist, cleer
from tinydb import TinyDB, Query
from rw import save_lists, showlists
from task import task
from tdlist import tdlist

def lsmenu():
    print("1.")
    print("2.")
    print("3.")
    print("4.")
    print("5.Exit")
    return int(input(">"))

def lsman():
    while True:
        choice = menu()
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            cleer()
            return main()