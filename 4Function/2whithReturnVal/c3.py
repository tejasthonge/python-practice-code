



def printVal(x,y,z):
    x+=10
    y+=10
    z+=10
    return x,y,z

val1 = int(input("enter the value 1 :"))
val2 = int(input("enter the value 2 :"))
val3 = int(input("enter the value 3 :"))

a,b,c = printVal(val1,val2,val3)
print(a)
print(b)
print(c)

print(type(a))

