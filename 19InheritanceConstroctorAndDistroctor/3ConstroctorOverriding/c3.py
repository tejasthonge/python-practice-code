



class Parent:

    def __init__(self):
        print(id(self))
        print("in constroctor parent")

    def parentFun(self):
        print("in parent fun")



class Child(Parent):

    def __init__(self):
        print(id(self))
        super().__init__()   #this line we have to write but in other lang it added by compiler 
        print("in chid constroctor")
        
    def childFun(self):
        print("in childFun")


obj = Child()

'''
boss% python3 c3.py
140470281207088
140470281207088
in constroctor parent
in chid constroctor

'''
