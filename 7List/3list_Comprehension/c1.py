

#Comprehension
#   -it is techanique to write the list without using any third party laibarory


normalList = [num for num in range(1,11)]

print(normalList)
print(type(normalList))


#creating squre list 

sqrList = [num*num for num in range(1,11)]
print(sqrList)

#####

even_List = [num*num for num in range(1,11) if num%2==0 ]  #it store only even vlaues in the list  
print(even_List)


 
