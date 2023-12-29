


#Inheritance:

'''
--python suppert by defoualt inheritace
--object class is by defoalt parent of the any class 


--by using childClass(parentClass)  this we can make parent of any class

'''

class Parent:

    def __init__(self):
        print("in parent constroctor")

    def fun(self):
        print("in parent fun")

class Child(Parent):
    pass

obj = Child()  #creating the child class object but
obj.fun()    #it calling the parent class method means it inherit all the varables and method from their parent class
