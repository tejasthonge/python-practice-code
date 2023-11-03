


def outer():
    print("in outer fun")
    def inner():
        print("in inner")


print("start code")
outer()
print("end code")
