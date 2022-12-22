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

class supermarket:
    '''this is my supermarket'''
    def__init__(self.x,y,z=none):
        self.brand=x
        self.price=y
        self.discount=z
        print("check me check me")
bread=supermarket("abc",25,25)
print(bread.brand)
biscuit=supermarket("pqr",10.50,25)
shampoo=supermarket("xyz",5,25)
rice=supermarket("seeragachamba",65)
print(rice.discount)


class supermarket:
    '''this is my supermarket'''
    manufacturer='muthu supermarket'
    marketer='msm'
    def__init__(self,x,y,z=none):
        self.brand=x
        self.price=y
        self.discount=z
        print("check me check me")
bread=supermarket("abc",25,25)
print(bread.brand)
biscuit=supermarket("pqr",10.50,25)
shampoo=supermarket("xyz",5,25)
rice=supermarket("seeragachamba",65)
print(rice.discount)


class theatre:
    '''this is my theatre'''
    def __init__(self,show_timeing.ticket_price):
        self.show_time=show_timeing
        self.ticket_price=ticket_price
master=theatre(2.30,150)
easwaran=theatre(6.00,6.00)
print(master.__dict__)


class customer:
    '''customer of bank'''
    def deposit(self,amt)
        print("you are going to deposit ",amt)
rajarajan=customer
rajarajan.deposit(500)

class test:
    a=100
    def __init__(self):
        self.b=200
t=test()
print(t.b)
print(t.a)
t.a=777
print(t.a)
print(test.a)


functions = methods 

types of methods:
    #instance methods
    #class methods
    #static methods

#instance methods

*sample->memory reference-->object
*instance variables-->object variables-->self
*object called python key word = self
*function create key word= def 
*self<--object<--instance variable


class student:
    def __init__(self,name,marks):
        self.name =name
        self.total=marks
    def display(self):
        print('hi',self.name)
stud1=student('ganesh',450)
stud1.display()


class supermarket:
    '''this is my supermarket'''
    manufacturer='muthu supermarket'
    marketer='msm'
    def__init__(self,x,y,z=none):
        self.brand=x
        self.price=y
        self.discount=z
        print("check me check me")
bread=supermarket("abc",25,25)
print(bread.brand)
biscuit=supermarket("pqr",10.50,25)
shampoo=supermarket("xyz",5,25)
rice=supermarket("seeragachamba",65)
print(rice.discount)
rice.manufacturer='rice mill'
print(rice.manufacturer)
print(suppermarket.manufacturer)
print(shampoo.manufacturer)


class office:
    noofholidays=10
    @classmethod
    def checkholidays(cls,branch):
        print("this year our",branch,'has',cls.noofholidays)
office.checkholidays('chennai')
office.checkholidays('bengaluru')


#class methods
    1.inside function definition ,only class specific variable(static varoables)used 
    2.class specific methods -@classmethod
    3.cls variable
    4.can call class name by using class name or object reference 

#static methods(utiluty methods)
    *utility methods

class calculater:
    @staticmethod
    def add(no1,no2):
        print('result is ',no1+no2)
calculator.add(100,200)
    *self ,cls no using this function
    *omly using local variable dont using anothor method  .that is static methods 
     *local variable =no1,no2


@class method          - @staticmethod
*arguments cls          -  *no cls -no self 
*class level variables  -  *local variable are used
*are used                - *utitlty methods 


today class topic 
    *class 
    *object
    *constructor 
    *types of methods-instance methods,class ,local
    *types of methods -object(instance),class ,local
    *@classmethod,@staticmethod



