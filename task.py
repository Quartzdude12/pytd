# task class

class task():
    def __init__(self, name, state):
        self.name = name
        self.state = False
    
    def solve(self):
        self.state = True
    
    def unsolve(self):
        self.state = False

    def aslist(self, name, state):
        return [self.name, self.state]

    def __str__(self):
        if self.state == True:
            return self.name, "Y"
        else:
            return self.name, "N"
    