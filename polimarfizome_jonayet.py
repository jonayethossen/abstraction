class Animal:
    def __init__(self,name):
        self.name = name
        print(self.name + "was adopted.")

def run(self):
    print("runnng!")    
class turtle(Animal):
    def run(self):
        print("runniing slowly!")

tim = turtle("tim")
tim.run()