#4. WAP for a function that returns the count of the search element in the list


def count(listData,ele):
    count = 0
    for i in listData:
        if ele == i:
            count+=1
    return count

print("enter the list bellow :" )

listData = [int(val) for val in input().split()]
print(listData)
ele = int(input("enter the element form above that you want find :"))

print("count of ", ele ," is : ",count(listData,ele))
