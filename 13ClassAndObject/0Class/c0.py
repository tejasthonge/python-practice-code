#OPP : in real time all are opp
'''
for example compny is class and it diffent work funciality or emmlyes and thir emp id as we it 
--employe have thir name and thir role and them have to work like funtion 



'''

#funtion : withount the class
#methon : inside the class

class Employe: 
    name = "bala"
    empId = 22
    sal = 1.3

    def work(self):#error required one parametor of Employe 
        print("frontend dev.")

obj = Employe()
print(obj);
print(type(obj))
#obj.wort() #type error
obj.work()
    
