'''
9. WAP to print squares of even numbers up to n.
Input: 10
Output: 4 16 36 64 100.
'''


n  = int(input("enter the no upto squre of even is print : "))
i = 1
while i <= n:
    if i%2 == 0:
        print(i*i,end =" ")
    i+=1
