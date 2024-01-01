


class Demo:

    def __init__(self):
        print("in constructor")

    def __del__(self):
        print("in destructor")

obj = Demo()

# as obeject created fist call is to the constructor this call is take place implisety

#like that destructor is work but it call or notify when object will relise means onject will be free the addresss of tha object 
#destructor also call implisety means automatic like constructor

#supose we create anather objet then call will be taken two times

obj1 = Demo()

