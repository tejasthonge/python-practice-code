

#if child not writ the constorctor


class Parent :

    def __init__(self):
        print("in parent constroctor")
        print(id(self))

class child(Parent):

    def fun(self):
        print("in child fun")
        print(id(self))


obj = child()
obj.fun()


'''
op:
in parent constroctor
139625271558096
in child fun
139625271558096

note:
    --both id has same means it child class not write own constroctor it inherit by its parent class


'''
