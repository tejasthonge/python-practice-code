

class Demo:
    x= "class variable"

    def __init__(self):
        self.y = "instance veraible"
    @staticmethod
    def fun():
        #print(x) #NameError: name 'x' is not defined
        print(Demo.x)
        #instance varible not accasible

        print("in static method fun")

print("start main")
obj = Demo()
Demo.fun
obj.fun()
