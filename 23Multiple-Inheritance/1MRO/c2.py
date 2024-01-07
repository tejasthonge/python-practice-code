#MRO:
'''
method resolition order 
--to handele the multiple inheritnce

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

class Demo:
    pass


print(Demo.mro) #<built-in method mro of type object at 0x559a140eec60>  it print the abut mro

print(Demo.mro())  #call to mro 



class Remo(Demo):
    pass

print(Remo.mro())

'''
<built-in method mro of type object at 0x562aa6037f80>
[<class '__main__.Demo'>, <class 'object'>]
[<class '__main__.Remo'>, <class '__main__.Demo'>, <class 'object'>]


'''








