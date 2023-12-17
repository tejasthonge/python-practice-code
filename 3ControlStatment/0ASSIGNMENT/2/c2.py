

'''
2. WAP to determine whether entered angles define a right-angled triangle.
Take three values of angle from the user.
Input1: angel1 = 90
Input2: angle2 = 90
Input3: angle3 = 90
Output:
It is not a right-angle triangle
Input1: angel1 = 90
Input2: angle2 = 60
Input3: angle3 = 30
Output:
It is a right-angle triangle

'''

a1 = int(input("enter the angel 1 : "))
a2 = int(input("enter the angel 3 : "))
a3 = int(input("enter the angel 3 : "))

if (a1 ==90 or a2 ==90 or a3==90) and( a1+a2+a3==180):
    print("it is right angel trungle")
elif a1+a2+a3 != 180:
    print("its not tringle")
else :
    print("it is not rigth angele tringele")
