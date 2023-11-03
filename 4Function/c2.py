#functon who return function

def outer():

    def inner():
        print("in inner fun")

    print("in outer fun")
    return inner

print("start code")
call = outer()   #her call veravle store the return value of outer fun

print(call)#it print addres of the inner function


##we can call the call
call()  #mens call is callable type
print("end code")
