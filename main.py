# pytd by CAA aka Betrayed_ aka Quartzdude12
# WE REWRITING IT IN RUST WITH THIS ONE RRRRRRRRRAAAAAAAAAHHHHHHHHH
import os
import sys
from functions import mktsk, mklist, cleer
from tinydb import TinyDB, Query
from rw import save_lists, showlists
from task import task
from tdlist import tdlist
from lsman import lsman

def menu():
    print("1.Show all lists")
    print("2.Load List")
    print("3.Save List")
    print("4.Manage Lists")
    print("5.Exit")
    return int(input(">"))

def main():
    while True:
        choice = menu()
        if choice == 1:
            showlists()
        elif choice == 2:
            showlists()
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            cleer()
            break

cleer()
main()