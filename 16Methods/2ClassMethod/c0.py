
#Class method :

'''
the memodry alloction is inside the class name space theis callad as class method 

class method is accassible by both the object or the class

'''


class Demo:

    @classmethod
    def fun():
        print("in class method")

obj = Demo()
Demo.fun()  #it gives error the riion the

'''
TypeError: Demo.fun() takes 0 positional arguments but 1 was given
'''
