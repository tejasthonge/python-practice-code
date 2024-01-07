

class Data:
    pass

obj =Data()


print("---------object class---------")
print(dir(object))

print("---------type class---------")
print(dir(type))

print("---------Data class---------")
print(dir(Data))

print("---------object of class Data---------")
print(dir(obj))





'''
OP

---------object class---------
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
---------type class---------
['__abstractmethods__', '__annotations__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__', '__or__', '__prepare__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__setattr__', '__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signature__', '__weakrefoffset__', 'mro']
---------Data class---------
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
---------object of class Data---------
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']


'''

#object class:
'''
1.it has parent of all the class in python3 
2.all are methods in python means 
--we know methods are object
for eg:
    in object class have __eq__ it methosd callad as dundure method that is dubleundscore method
    this method is callad when we use == oprator 
    --means this is oparator overloding concept 
    we print(a==b)  it intenlay call to -->   a.__eq__(b)  
    eg2:
        we call dir(Demo)  we call to __dir__  as -->    __dir__(Demo)
      
    means this dir meethod is class object and inherted by thire child class
    and it return the what are methods in the contont(magic method in class)
3.mro :
    is not present in object class 
'''

#type class:
'''
--type class is type or strcture of how class differ form each other 
--type is like sachy :
    --means to create ganpti bappa murtie it use sache of that time 
    --to antore type murti we use anthor type sachya

-- so all the class is by defoat type type class
--means We write Demo class and print thire type it print class 'type'
we print(type(object)) it print --> class 'type'  means object class also type type class
--or we by defalr object class is parent so all the class are type type class 


#MRO:

    it theis type class hase __mro__ that is method rosolution order
    --it print how the oreder of assing the mehtods form their multiple paret parent class 
    --python3 mro use -->C3linerizetion algorithum itermaly to tuch tire multiplle pasrent and accasse the method without ambibuty

    --this is mejor change in all version or other progaminng langwage to supart multipele inhertance by defoalt

'''



