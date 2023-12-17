'''
5. Print the "Core2web" string a number of times entered by the user if the
number is even.
#Input: num = 2
#Output: Core2web
Core2web
#Input: num = 5
#Output: No Output

'''

times = int(input("enter no times "))

if times%2==0:
    for i in range(0,times):
        print("core2web" )


