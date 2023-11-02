#print : 5 * 15 * 25 * 35 * 45 *


for i in range(50):
    
    if(i%5==0):
        if(i%2!=0):
            print(i ,end=" ")
        else:
            print("* ",end="");
print();
