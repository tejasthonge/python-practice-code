

def fun():
    print("in fun")

    def inner():
        print("in inner")

    def inner1():
        print("in inner1")
    return inner ,inner1  #we can return mullitiple value in form of tuple

print("start")
ret,ret1 = fun()

ret()
ret1()
