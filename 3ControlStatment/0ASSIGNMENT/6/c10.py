

'''
10. WAP to print a cube of odd numbers up to n in reverse order.
Input: 15
Output: 3375 2197 1331 729 343 125 27 1
'''

n = int(input("enter the n :"))

while n!=0:
    if n%2!=0:
        print(n*n*n,end=" ")
    n-=1
