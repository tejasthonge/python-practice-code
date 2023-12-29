



class parent:
    def __init__(self):
        print("in parent constrctor 1")

    def __init__(self):  #it not gives error like other proLang 
                            #it override constroctor 1 body

        print("in parent constroctor 2")


obj = parent() #it calling to second constroctor not to the first

'''

OP:

    in parent constroctor 2

    '''



