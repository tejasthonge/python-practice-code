

#Instance Method:

'''
it address in object 
-- object created it initilize inside the object in object Name space
--it is only accasses by the object of that class
--self is requre for instance method
--not call by the class name 

'''

class Home:
    tv = " tv is off "

    def __init__(self,name):
        self.name =name

    
    def jevan(self):
        print("instance method")
        print(self.name," : j1 vadhal ya ..!")
        

print("start main")

ai = Home("ai")
papa = Home("papa")
didi= Home("didi")
mi = Home("mich")

print(didi.tv)

ai.jevan()

mi.tv = "IPL watch on tv"
print(didi.tv)

papa.tv= "news wacthing on tv"
print(papa.tv) #news wching on tv
print(mi.tv) #ipl vathing on tv
print(didi.tv) #off

#but we chage by using class name then-->

Home.tv ="tv is on"

print(papa.tv) #news wching on tv  -->it also print the chige in thire object not in in class namespace 
print(mi.tv) #ipl vathing on tv
print(didi.tv) #off  ---it will chaneget the rision in class namesvace value change this value is same as copy in object name space



print("end main")



