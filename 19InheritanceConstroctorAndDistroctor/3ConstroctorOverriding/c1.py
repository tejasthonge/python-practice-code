

#constructor overriding:

class Parent:

    def __init__(self):
        print("in constructor")

    def fun(self):
        print("in parent fun")


class Child(Parent):

    def __init__(self):
        print("in child constroutor")


obj = Child()
obj.fun()


'''

op:

in child constroctror
in parent fun


note:
    --means other ProgLang hase fist line that call to parent constroct inside the child constroctor 

    --but in python it override the parent costroctor
    --means all the method and varable are inheted by theire child but the constor is also
    mehtod so it also inheriated by child class by in child class it write it own constroctor so so it will replse by new constrorctor that is child constroctor 

'''



