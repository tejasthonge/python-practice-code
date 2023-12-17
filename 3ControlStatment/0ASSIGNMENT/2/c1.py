#Assignment 2

'''
1. WAP to check numbers are divisible by 4 and 5
Print those numbers
Input1: num1 =20
Output:
20 is divisible by 4 and 5
Input1: num1 =15
Output:
15 is not divisible by 4 and 5

'''

n = int(input("enter the no :"))

if n%4==0 and n%5==0 :
    print(n," is divisible by 4 and 5")
else :
    print(n ," is not divisible by 4 and 5")
