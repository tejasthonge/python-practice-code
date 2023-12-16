


#Static methods:

'''
--the method not instane or not class methods is callad as statcickey word

'''

class Demo:

    
    @staticmethod
    def fun():
        print("in static method fun")


print("stat fun")
obj = Demo()

#both can accassised
Demo.fun()
obj.fun()
