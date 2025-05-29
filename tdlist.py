# task list class

from functions import *
from tinydb import TinyDB, Query
from functions import *
from task import task

class tdlist():
    def __init__(self, tasks, name):
        self.name = name
        self.tasks = []
    
    def addtsk(self):
        self.tasks.append(mktsk())
    
    def showtsk(self):
        print(self.name)
        for i in range(len(self.tasks)):
            print(self.tasks[i])
    
    def remtsk(self):
        print("Current list:")
        self.showtsk()
        remaddr = int(input("Task number to remove: "))
        remaddr = remaddr - 1
        del self.tasks[remaddr]
        print("Result:")
        self.showtsk()
    
    def swaptsk(self):
        print("Current list:")
        self.showtsk()
        startaddr = int(input("Select item to move: "))
        destaddr = int(input("Select item to swap with: "))
        startaddr = startaddr - 1
        destaddr = destaddr - 1
        if 0 <= startaddr <= len(self.tasks) and 0 <= destaddr <= len(self.tasks):
            self.tasks[startaddr], self.tasks[destaddr] = self.tasks[destaddr], self.tasks[startaddr]
            return startaddr, destaddr
        else:
            print("Index out of range, try again")

    def __str__(self):
        return f"{self.name}"

    def to_dict_of_dicts(self):
        return {
            'name' : self.name,
            'tasks' : [task.to_dict for task in self.tasks]
        }

testbed = tdlist([], "testbed")
testbed.addtsk()
testbed.addtsk()
testbed.addtsk()
testbed.addtsk()
testbed.showtsk()
testbed.swaptsk()
testbed.remtsk()
print(testbed)