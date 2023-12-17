

'''
Program5 :
Row = 4
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

'''

row = 4 

k=1
for j in range(0,row):
    m=k
    for i in range (1,row+1):
        print(m,end=" ")
        m+=1
    k+=1
    print()
