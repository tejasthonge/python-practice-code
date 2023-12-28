


def gun():
    print("in gun")

def run(y):
    print("in run")
    y()

def fun(x):
    print("in fun")
    x()

fun(run(gun))

'''
op:
    in run
in gun
in fun
Traceback (most recent call last):
  File "/home/amarraj/python-prctice-codes/17Decorator/c2.py", line 15, in <module>
    fun(run(gun))
  File "/home/amarraj/python-prctice-codes/17Decorator/c2.py", line 13, in fun
    x()
TypeError: 'NoneType' object is not callable

'''
