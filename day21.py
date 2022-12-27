day21 
    INHERITANCE- SINGLE-MULTILEVEL - MULTIPLE

inheritace:
    an object of one class behaving as an object of another class

class humanbeing:
    def __init__(self.name,age)
        self.name=name
        self.age=age
    def readingbooks(self):
        print('readingbooks')
#instance method two instance variable
class enployee(humanbeing):
    def __init__(self,name,eno,salary):
        super().__init__(name,age)
        self.empid=empid
        self.salary=salary
emp1=employee('celin',22,101,30000)
print(emp1)    ----->  <__main__ class name object at ox988884rt754>
    *object is memory reference 

1)if l print an object ,memory ref.of the objects will be printed   True/False
2)in print,everthing is object   True/False
3)hence,if i print anything in python , memory ref will get printed.  True/False

# single inheritance

class humanbeing:
    def __init__(self.name,age)
        self.name=name
        self.age=age
    def readingbooks(self):
        print('readingbooks')
#instance method two instance variable
class enployee(humanbeing):
    def __init__(self,name,eno,salary):
        super().__init__(name,age)
        self.empid=empid
        self.salary=salary
        
        def __str__(self):
            return 'name={}\n salary={}'.format(self.name,self.salary)
emp1=employee('celin',22,101,30000)
print(emp1)


# multilevel inhertance

class grandparent:
    def agriculture(self):
        print('watering plants')
class parent(grandparent):
    def readingbooks(self):
        print('reading books')
class child(parent):
    def doingexercise(self):
        print('doing exercises regularly')
c=child()
c.doingexcercise()
c.readingbooks()
c.agriculture()


# hierarchical inheritance

class honda:
    def givesalary(self):
        print('honda salary')
class bikes(honda):
    def designbikes(self):
        print('honda bikes')
class cars(honda):
    def designcars(self):
        print('honda cars')
emp1=bikes()
emp1.designbikes()
emp2=cars()
emp2.designcars()
emp3=bikes()
emp3.designcars()
emp4=cars()
emp4.designbikes()



class father:
    def drawing(self):
        print('drawing')
class mother:
    def goingtojob(self):
        print('mother going to job')
class child(father,mother):
    def studying(self):
        print('child is studying')
        father.goingtojob(self)

c=child()
c.studying()
c.drawing()
c.goingtojob()
father.goingtojob(self)


class father:
    def drawing(self):
        print('drawing')
class mother:
    def goingtojob(self):
        print('mother going to job')
class child(mother,father):           # changing to (mother ,father)
    def studying(self):
        print('child is studying')
        father.goingtojob(self)

c=child()
c.studying()
c.drawing()
c.goingtojob()
father.goingtojob(self)


class parent:
    i=100
    def __init__(self):
        self.j=200
class C(parent):
    def mi(self):
        print(super().i)
#        print(super().j)-->error
        print(self.j)
c=C()
c.mi()





class parent:
    i=100
    def __init__(self):
        self.j=200
        print('hi, i am super class constructor')
class C(parent):
    def __init__(self):
        super().__init__()
        super().test()
    def mi(self):
        print(super().i)
#        print(super().j)-->error
        print(self.j)
c=C()
c.mi()



class parent:
    i=100
    def __init__(self):
        self.j=200
        print('hi, i am super class constructor')
    def test(self):
        print('testing in super class')
    @staticmethod
    def test2(self):
        print('parent static method')
    @classmethod
    def test3(cls):
        print('parent class method')
class C(parent):
    def __init__(self):
        super().__init__()
        super().test()
        super().test2()
        super().test3()
    def mi(self):
        print(super().i)
#        print(super().j)-->error
        print(self.j)
        super().test()
        super().test2()
        super().test3()
    @classmethod
    def display(cls):
        super().test()
        super().test2()
        super().test3()
    @classmethod
    def display(cls):
        super(C.cls).test(cls)
c=C()
c.mi()



*super()--->super class level variable,super class --->instance variable
*super()--->fron child class constructor and child class instance method,using
    super()-->accessing all types of methods (static ,class ,instance)in super class
*fron child class ,class methods -->accessing parent class instance methods and constructors using super() is not possible


#polymorphism -many forms

print('hi'+'5')
print(5+5)
print('hi'*3)
print(5*3)

operator overloading
method overloading
constuctor overloading
method overraiding
constructor overriding
inheritance (very important)
duck typing


class bike:
    def fill(self):
        print('fill petrol')
class lorry:
    def fill(self):
        print('fill diesel')
class ecar:
    def fill(self):
        print('fill power')
def charge(obj):
    obj.fill()
b=bike()
l=lorry()
c=ecar()
list=[b,l,c]
for obj in list:
    charge(obj)


