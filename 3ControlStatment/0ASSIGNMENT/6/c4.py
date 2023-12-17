'''
4. WAP to calculate the factorial of a given number.
Input:
5
Output:
Factorial of 5 is 120

'''
i=1
n = 5
fact = 1

while i <= 5:
    fact *= i
    i+=1

print("Factorial of ",n ," is ",fact)
