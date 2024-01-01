
#Destroctor:
'''
--it is spcial method 
--it call implysety to __del__ at time of object reface is removed
--it is writen by __del__
--

'''

'''
Differance bettewen  Destroctor and garbage colletor

De

'''



class Parent :


    z= 30
    def  __init__(self):
        print("in parent constructor")

        self.x=100
        self.y=200

    def dispData(self):
        print(self.x)
        print(self.y)

    @classmethod
    def dispParent(cls):
        print(cls.z)

    def __del__(self):
        print("in Destroctor")

obj = Parent()
obj.dispData()
obj.__del__()  #it call by defoualt when the object is relesed form the memory means the  momory the object refarence will removed 


#destor has work that is notify the object refarancee will remove
