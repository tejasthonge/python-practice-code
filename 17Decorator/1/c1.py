



def decorFun(fun):

    def wrapper():
        print("start wrapper")
        fun()
        print("end wrapper")

    return wrapper

def normalFun():
    print("hello in normal fun")
    
normalFun= decorFun(normalFun)   #the return value of the decorFun is wrapper function so but the normal nunction is change and add some functionality on it
normalFun()   #it add extra two line that is start wrapper end wrapper and the call of the normalFun is inside tha wrapper function the but currently wrarrer functions addreess store in normalFun ..

