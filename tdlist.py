# task list class

from functions import *
from tinydb import TinyDB, Query

tdb = TinyDB('tdb.json')

class tdlist():
    def __init__(self, tasks, name):
        self.name = name
        self.tasks = []
    
    def addtsk(self):
        self.tasks.append(mktsk())
    
    def showtsk(self, tasks, name):
        print(self.name)
        for i in range(len(self.tasks)):
            print(i+1,self.tasks[i])
    
    def remtsk(self, tasks, name):
        print("Current list:")
        showtsk()
        remaddr = int(input("Task number to remove: "))
        del self.tasks[remaddr]
        print("Result:")
        showtsk()
    
    def swaptsk(self, tasks, name):
        print("Current list:")
        showtsk()
        startaddr = int(input("Select item to move: "))
        destaddr = int(input("Select item to swap with: "))
        if 0 <= startaddr <= len(self.tasks) and 0 <= destaddr <= len(self.tasks):
            self.tasks[startaddr], self.tasks[destaddr] = self.tasks[destaddr], self.tasks[startaddr]
            return startaddr, destaddr
        else:
            print("Index out of range, try again")

