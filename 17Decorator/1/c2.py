
# from tha befor code we can say wat actyluly happen but theis is seen by eye by 
# using the Decorator we can handder it by adding juct @ and fuction name upper the functon 


#Decorator :

'''

-- it  add some extra functionality on it 
-- we call same function but inside that function this calling to anthor function 
    due decorator this can be handdele the 
--in python decorator is an class and 

'''

def decorFun():

    def wrapper():
        print("start ")
        #fun()
        print("end")

    return wrapper
@decorFun
def normalFun():
    print("in noraml fun")

normalFun();
