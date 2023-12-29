



class Demo:

    def __init__(self):
        self.x= 10
        self.y= 20
        print("in constructor")

    def setData(self,z):
        self.z= z  #it is also insance varable but the acutuale memory or value for z will be after the calling the setData or passing the arrgumet to the method 
        


    def printData(self):
        print(self.x)
        print(self.y)
        print(self.z) #we assesing z instance varable before the it intiolize
                        #but


obj = Demo()
obj.printData()

'''
OP:

in constructor
10
20
Traceback (most recent call last):
  File "/home/amarraj/python-prctice-codes/19InheritanceConstroctorAndDistroctor/c0.py", line 23, in <module>
    obj.printData()
  File "/home/amarraj/python-prctice-codes/19InheritanceConstroctorAndDistroctor/c0.py", line 19, in printData
    print(self.z)
AttributeError: 'Demo' object has no attribute 'z'
'''



