#Multiple Inheritace :


'''
--python suport multiple in heritace
--in othar lang not suport 
--we have to use interface or mxine if we have two parent of class 

'''
#MRO:
'''
--Method Redoluton Orader 
--by using ineterny this we can hander the multiple inheritace in pyhton
--in puython2 and python3 mro are differnt the resion is it use different algo. depeding on verion

'''



class Parent1:

    def dispData(self):
        print("in parent1 dispData")

class Parent2:

    def printData(self):
        print("in parent2 printData");

class Child(Parent1, Parent2):
    pass 

    '''
        -- in child class its own is nothing
        -- but it have two parent class 
        -- so it inherite form this 
        -- all of the parent class is inherted by child class
        -- so Child class hase two method 
    '''


obj = Child()

obj.dispData()  #call parent1 method
obj.printData()  #call parent2 method


'''
OP:
in parent1 dispData
in parent2 printData
'''

