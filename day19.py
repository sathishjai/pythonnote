object oriented programing -object class -constructor methods-variables types.

class student:
    '''this class is about student'''
print(student.__doc__)
help(student)

class supermarket:
    ''' this is my supermarket'''
bread=supermarket()
biscuit=supermarket()
shampo=supermarket()
rice=supermarket()


class supermarket:
    ''' this is my supermarket'''
bread=supermarket()
bread.brand='abc'
bread.price=25
biscuit=supermarket()
biscuit.brand='pqr'
biscuit.price=10
shampo=supermarket()
shampo.brand='xyz'
shampo.price=5
rice=supermarket() 
rise.brand='seeraga chamba'
rice.price=65
print(rice.price)
print(biscuit.__dict__)

class supermarket:
    ''' this is my supermarket'''
    def __init__(self,brand,price.discount)   #formal parameters
        self.brand=brand
        self.price=price
        self.discount=discount
        print("check me check me check me"
bread=supermarket("abc",25,25)   #actual parameters
print(bread.brand)
biscuit=supermarket("pqr",10,25)
shampo=supermarket("xyz",5,25)
rise=supermarket("seeragachamba",65)

__init__ is called automatically when the object is created 
__init__ =constructor
    special function
    constructor is getting called /invoked automatically whenever we create object
    initializing object specific information


