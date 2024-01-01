

class Demo:

    def __init__(self):
        print("in constructor")

    def __del__(self):
        print("in destructor object deleated")


obj1 =Demo()

obj2= Demo()

obj3 =obj1

del obj1 #deleting the object

#we calling to delet the objectect obj1 but the refacre is also store in obj3 so object obj1 or obj3 both are pointer towards the same object but obj1 is deleted means only reface is cut of obj1 but other refance is store in obj3 so it not call to destructor

print("end")
'''

OP:
in constructor
in constructor
end
in destructor object deleated
in destructor object deleated


//it not print at time of deleting the obj1 
'''

