'''continue:
        --Statment is used for the continue the etaration
        -- this is work only on loops
        --not working on the conditions
        --it just similar as pass statement but not same as that
'''


#write the code print odd no range 10 and print them without that
#op: 1,3,5 ,7,9
#by uding only the continue 


for i in range(10):
    if(i%2==0):
        pass;
    else:
        print(i ," ");

#by using the contine

print("-------");
for i in range(10):
    if(i%2==0):
        continue;
    else:
        print(i ," ");

'''
note that coninue contues the whole the etration but pass just pass that condition
'''


