


def run():
    print("in run")

def fun(x):
    x()
    print("in fun")

fun(run)

'''

op:
    in run 
    in fun
    '''
