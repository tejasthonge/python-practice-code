

class Employee:
    def __init__(self,empId,empName):
        self.empId =empId
        self.empName = empName

    def disp(self):
        #print(empId)   #cant accses directly
        #print(empName)    #cant accasses directu
        #self is for that accasset insrtance varible or it self ---> address of new object
        print(self.empId ," : " ,self.empName)
#        print(self.empName)

def fun():
    print("in fun")
fun();  
emp1 = Employee(10,"shreyash")
emp2 = Employee(11,"bala")

emp1.disp()
emp2.disp()
