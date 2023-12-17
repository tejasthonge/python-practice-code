'''
. Take two numbers from users and print the sum of those numbers
if the sum is even.
Input1: num1 = 10
Input2: num2 = 20
Output: 30 is Even
Input1: num1 = 10
Input2: num2 = 15
Output: No Output
'''


num1 = int(input("enter the no1 : "))
num2 = int(input("enter the no2 : "))

if (num1+num2)%2==0 :
    print(num1+num2 ," is even")
else:
    print(" is odd")
