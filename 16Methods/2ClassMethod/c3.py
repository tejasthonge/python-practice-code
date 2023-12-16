

class Demo :
    x = "class varaible"
    
    def __init__(self):
        self.y ="init varible"

    def instanceMethod(self):
        print("in instance method")
        #accassing the instance varivle 
        print(self.y) #call by object -->
#        print(Demo.y) #call by class -->  not accassible by the class name errr:AttributeError: type object 'Demo' has no attribute 'y'
    
        '''we can accasses the both class as we as instace vaerible in instace method'''
    
        #accassing the class varible
        print(self.x)
        print(Demo.x)
        #print(x)  -- not accassible by this way

    @classmethod
    def classMethod(cls):

        #accassing the instance varivle 
       # print(cls.y) #call by cls-->  error
        #print(Demo.y) #call by class --> error

        ''' we can not accaset the instanc varible in class method '''

        #accassing the class varible
        print(cls.x)
        print(Demo.x)
   #     print(x)

obj = Demo()

obj.instanceMethod()
#Demo.instanceMethod() #error
print("----------")
obj.classMethod() 
Demo.classMethod()
