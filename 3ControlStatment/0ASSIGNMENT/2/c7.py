'''
7. Take two numbers from the user, check if both are odd and then print the
sum of the numbers.
#Input: num1 = 10
#Input: num2 = 11
#Output: 21
#Input: num1 = 10
#Input: num2 = 6
#Output: No Output

'''

n1 = int(input("n1 : "))
n2 = int(input("n2 : "))

if n1%2!=0 or n2%2!=0 :
    print(n1+n2)
