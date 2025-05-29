# task class

class task():
    def __init__(self, name, state=False):
        self.name = name
        self.state = state
    
    def solve(self):
        self.state = True
    
    def unsolve(self):
        self.state = False

    def __str__(self):
        if self.state == True:
            return f"{self.name} Y"
        else:
            return f"{self.name} N"

    def to_dict(self): #turn into dict for tinydb
        return {
            'name' : self.name,
            'state' : self.state
        }
    