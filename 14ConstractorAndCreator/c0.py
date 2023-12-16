#creator:
'''
it hase wor to creat the object on memory area 

'''

#constroctor:
'''
it initionlize the value to vairable and give the memory in side the init means in constroctor 
--constroctor is present in the object and and object hase memory area

'''


class Demo:
    def __new__(self):
        print("creator")
        return object.__new__(self)  #we use super() replase of object

    def __int__(self):
        print("constroctor")

obj = Demo();
