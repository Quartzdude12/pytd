# A

import pickle
import os

def cleer():
    os.system('cls' if os.name == 'nt' else 'clear')

class task():
    def __init__(self, name, state):
        self.name = name
        self.state = False
    
    def solve(self):
        self.state = True
    
    def unsolve(self):
        self.state = False

    def __str__(self):
        if self.state == True:
            return "Y"
        else:
            return "N"

def mktsk():
    tskname = str(input("Enter task name: "))
    return task(tskname, False)

def mklist():
    listname = str(input("Enter list name:"))
    return tdlist([], listname)

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
        else:
            print("Index out of range, try again")

    def savepkl(self):
        with open("pytd.pkl", "wb") as f:
            pickle.dump(self, f)
    
    def loadpkl(self):
        pass
    





