
class A:
    def fun(self):
        print("in fun : A ")
class B:
    def fun(self):
        print("in fun : B ")
class C:
    def fun(self):
        print("in fun : C ")


class D(A,B):
    def fun(self):
        print("in fun : D ")
        super().fun()

class E(B,C):
    def fun(self):
        print("in fun : E ")
        super().fun()

class F(D,E) :
    def fun(self):
        print("in fun : F ")
        super().fun()



obj = F()
obj.fun()

'''
OP:
in fun : F
in fun : D
in fun : A


'''
