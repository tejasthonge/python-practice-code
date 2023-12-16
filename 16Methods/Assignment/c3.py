
#3. WAP for function returns the array of factorial of the element

import array as arr

def retArrOfFact(arr):
    
    i= 0
    for el in arr:
        
        fact =1 
        for val in range(1,el+1): 
            fact = fact*val
        arr[i] = fact
        i +=1
    return arr



arrayData = arr.array('i',[2,5,7,3,4])

for i in arrayData:
    print(i ,end = " ")

print()

for i in retArrOfFact(arrayData):
    print(i ,end = " "),
