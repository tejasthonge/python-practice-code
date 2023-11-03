


def outer():

    def inner():
        print("inner fun")

    inner()
    print("outer fun")

print("start code")
outer() 
print("end code")
