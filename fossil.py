import os
import json
from datetime import datetime

td = ["do the dishes", "eat the flesh", "have fun"]

def main():
 pass

def addtask():
 swptsk = input("Task to add:")
 td = td.append(swptsk)

def showlist():
 print("TO DO")
 for i in range(len(td)):
  print (f"{i + 1}.", td[i])

def remtask():
    print("Current list:")
    showlist()
    torem = int(input("Select item to remove: "))
    del td[torem]

def addattr():
    pass

showlist()
remtask()
showlist()