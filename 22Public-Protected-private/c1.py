


#private:

'''
--private internaly use namemanaling 

#namemannaling :
    -- changing the name of the varble by adding same unque key
    
--private are only assible for same class of same block
--but python intenaly use namemanalin so we can accassed by  using changed name
--it can write by using the '__'  double underscore
        eg: __x=10

--  _Demo__x = 10 here Demo x is demo class varable 
--if we print by using print(_Demo__x) it will print 10 mens private can be accassible
'''

#public :

'''
--by defoal all ar public in puthon 
-- means it accasseble all over

'''

#protected 

'''
-- is declere by the '_' single under score before the varable 
--projected is accasibble all over the same class as we child class 

'''





#code


class Demo:
    
    z =30  #public 
 
    def __init__(self):
        self._x = 10  #protected varible 
        self.__y= 20  #priavte varible

print(dir(Demo))  #dir it print the directry of Demo class what content

obj = Demo();
print(dir(obj)) 
#if we print it it can assible outside class 
print(obj._Demo__y)  #accssing the private varable


'''
op:

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'z']
['_Demo__y', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_x', 'z']
202020


'''

#abovw the output is of dir(Demo) and dir(obj)

#dir

'''

in obj dir it hase stor private varble y by using namemanling and the changed name is _Demo__y


'''
#if we print it it can assible outside class 
#print(Demo._Demo__y)  #accssing the private varable by calling on the class it geveserror the resion is it is instance vaible 
