

class A :
    pass

class B :
    pass

class C:
    pass

class AA(A,B):
    pass

class CC(B,C):
    pass

class ZZZ(AA,CC):
    pass

print(ZZZ.mro())

'''
OP:

    [<class '__main__.ZZZ'>, <class '__main__.AA'>, <class '__main__.A'>, <class '__main__.CC'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]


'''

#form above mro wee can undstand which method fist class 

