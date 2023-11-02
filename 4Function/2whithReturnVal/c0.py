

#function have return values

##python have spetial feture that is it have multiplpe return values



def printVal(x,y,z):
    x+=10
    y+=10
    z+=10
    return x,y,z

val1 = int(input("enter the value 1 :"))
val2 = int(input("enter the value 2 :"))
val3 = int(input("enter the value 3 :"))

print(printVal(val1,val2,val3));

