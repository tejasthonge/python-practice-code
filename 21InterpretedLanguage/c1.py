
'''

print :
    -- it is globale function that call form anay where

    we calling to the print function it will exucute firs inside the class 
    sepretinly or indpedtly

'''


class Demo:

    print("start class") #it print first 

    def fun(self):
        print("in fun")


print("start main")

obj = Demo()
obj.fun()
print("end fun")

