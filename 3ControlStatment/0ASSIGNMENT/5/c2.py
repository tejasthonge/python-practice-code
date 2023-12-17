'''
Program2 :
Rows = 4

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''

rows = int(input("enter no of rows : "))
k=1
for i in range(1,rows+1):

    for j in range(0,rows):
        print(k ,end= "  ")
        k+=1
    print()
