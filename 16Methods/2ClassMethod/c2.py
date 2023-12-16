

class Demo :
    
    @classmethod
    def fun(cls):  #this cls is requre we can rename it 
        print("in class method")
        print(type(cls))
        print(cls)

print("start main")
print(type(Demo))
print(Demo)

Demo.fun()

'''

start main
<class 'type'>
<class '__main__.Demo'>
in class method
<class 'type'>
<class '__main__.Demo'>
'''
