
#way to write instance varable without writing the constroctor 

'''
    --but the memory intializetion will take place after passing the value  but 
    thire is only  way to pass the value that is at time of calling the function

    --if we call printData befor the setData it gives error

    '''
class Demo:

    def setData (self,x):
        self.x=x   
  

    def printData(self):
        print(self.x)
    

obj = Demo()
obj.setData(10)
obj.printData()

print(obj.x)
#print(Demo.x) it geves attribute error if we call using class name 
'''
File "/home/amarraj/python-prctice-codes/19InheritanceConstroctorAndDistroctor/c1.py", line 22, in <module>
    obj.printData()
  File "/home/amarraj/python-prctice-codes/19InheritanceConstroctorAndDistroctor/c1.py", line 18, in printData
    print(self.x)
AttributeError: 'Demo' object has no attribute 'x'
'''

