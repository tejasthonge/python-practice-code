


class Demo:

    @classmethod
    def fun(cls):
        print("in class method")


obj = Demo()


#calling the class method 

#using class
Demo.fun()  #it run
#using object
obj.fun() #it run

'''
--means the class method can accassible by both class name and object also
--but the instanc method can not accassed by the class name 
--mens memory alloction of class method and instace method are different

class method -->in class namespace
instace method-->in object namespace

'''
