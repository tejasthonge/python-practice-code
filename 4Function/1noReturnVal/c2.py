
#write function to print the factorial of n



def printFact(n):
    fact=1;
    for i in range(1, n+1):
        fact*=i
    print(fact)

n = int(input("enter the no "))
printFact(n)
