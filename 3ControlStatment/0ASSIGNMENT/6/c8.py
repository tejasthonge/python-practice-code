
'''
8. WAP to print the sum numbers up to n.
Input: 10
Output: sum of numbers upto 10 is 55
'''

summ = 0

i =1
n = int(input("enter the n :"))

while i <= n:
    summ+=i
    i+=1
print("sum of first ", n , " is : ",summ)
