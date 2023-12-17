'''
3. WAP to find the 7th odd number (start from 1)
Output:
7th odd number is 13


'''

i= 1
n = 10
counter = 1
while i <=n*2+1:
    if counter == 7 :
        print(i)
    i+=2
    counter += 1 
