class Employe:
    name = "bala"
    empId = 22
    sal = 1.3

    def work(self:object,x):#error required one parametor of Employe 
        a = type(self)
        print(a)
        print("frontend dev.")

obj = Employe()
print(obj);
print(type(obj))
#obj.wort() #type error
obj.work(10)

