'''
7. WAP to find the nth even number.
Input: 3
Output: even number at position 3 is 5

'''

n = int(input("enter the nth possition"))
count =1
i= 2
while i<= n*2+1:
    
    if n==count :
        print(i)
    i+=2
    count+=1
