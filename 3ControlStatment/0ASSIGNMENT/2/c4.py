
'''
4. Take a number from the user and check whether it is present in the list. If
it's in the list, print "Available."
List1 = [10, 20, 30, 40, 50]
#input: num = 10
#Output: available
#input num = 15
#Output:No Output
'''

listData = [10,20,30,40,50]

num =  int(input("enter the no : "))

if num in listData:
    print("avilable")
