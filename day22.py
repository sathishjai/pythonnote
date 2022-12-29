DAY22
 
polymorphism -abstraction and encapsulation

#operator overloading

class book:
    def __init__(self,pages):
        self.pages=pages
    def__add__(self,another):
        return self.pages+another.pages
thirukkural=book(133)
thiruvasagam=book(200)
print(thirukkurakal+thiruvasagam)


# opeator overloading

+   ----> object __add__(self,another)      * another or other any one your chice
-   ----> object __sub__(self,another)
*   ----> object __mul__(self,another)
/   ----> object __div__(self,another)
//  ----> object __floordiv__(self,another)
%   ----> object __mod__(self,another)
**  ----> object __pow__(self,another)
+=  ----> object __iadd__(self,another)
-=  ----> object __isub__(self,another)
*=  ----> object __imul__(self,another)
/=  ----> object __idiv__(self,another)
//= ----> object __ifloordiv__(self,another)
<   ----> object __if__(self,another)
<=  ----> object __le__(self,another)
>   ----> object __gt__(self,another)
>=  ----> object __ge__(self,another)
==  ----> object __eq__(self,another)
!=  ----> object __ne__(self,another)

class mobiles:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def __gt__(self,other):
        retutn self.price>other.price
    #def __gt__(self,other):
        return self.price<other.price
    def __le__(self,other):
        return self.price<other.price
m1=mobiles("vivo",10000)
m2=mobiles("samsung",12000)
print(m1>m2)
print(m1<m2)


class mobiles:
    def __init__(self,brand,price,offer):
        self.brand=brand
        self.price=price
        self.offer=offer
    def __it__(self,other):
        return self.price<other.price
    def __add__(self,other):
        return self.offer+cc.offer
class crecitcard:
    def __init__(self,brand,ccoffer):
        self.brand=brand
        self.ccoffer=ccoffer
m1=mobiles("vivo",10000,1000)
m2=mobiles("samsung",12000,1000)
cc=creditcard("vivo",500)
print(m1+cc)


#method overloading:
same method name with different no of arguments
ex:
    def calculate(t,fe):
        pass
    def calculate(t,e,m):
        pass
    # LAST ONE CHOING PYTHON (any time two function same name last one select python )

class test:
    def calculate(self,*no):
        total=0
        for i in no:
            total=total+i
        print(total)
t=test()
t.calculate(10,20)
t.calculate(10,20,30)


class test:
    def calculate(self,no1,no2,no3=none):
        print('aaaa')
    def calculate(self,no1,no2,no3):
        print('bbbb')
t=test()
t.calculate(10,20)
t.calculate(10,20,30)


#comstructor overloading:

class suoermarket:
    def __init__(self,*constent):
ob1=supermatket("soap",20,2)
ob2=supermarket("rice",60)


#overriding

class parent:
    def study(self):
        print("engg or medical")
class child(parent):
    def play(self):
        super().study()
        print("playing kabadi")
    def study(self):
        print("humanities/science")
c=child()
c.study()

class parent:
    def __init__(self):
        print("parent class constructor")
    def study(self):
        print("engg or medical")
class child(parent):
    def __init__(self):
        print("child class constructor")
    def play(self):
        super().study()
        print("playing kabadi")
    def study(self):
        print("humanities/science")
c=child()
c.study()


#abstraction
    #showing only the necessary data and hiding unwanted

fron abc import*
class indian:
    @abstractmethod
    def havingbreakfast(self):
        pass
i=indian

#ABC---->Abstract base class
#abstract class --->class with at least one abstract method
#can't instantiate abstract class indian with abstract method havingbreak fast
#can't create object for
#object---->?


#*if we extend / inherit abstract class and we dont override the abstract methods present in parent class in that case ,child class is also considered as abstract and we couldn't instantiate(create object) for child class as well


from abc import*
class indian(ABC):
    @abstractmethod
    def havingbreakfast(self):
        pass
class tamils(indian):
    def havingdinner(self):
        print('eating pongal,idli')
class marati(indian):
    def havingbreakfast(self):
        print("vada pow")
t=tamils()
t.havingbreakfast()


from abc import*
class DBinterface(ABC):
    @abstractmethod
    def estaboshDB(self): pass
    @abstractmethod
    def disconnectDB (self): pass
class oraclleDB (DBinterface):
    def estabishDB(self):
        print("oracle DB connection")
    def disconnectDB(self):
        print("oracle DB disconnection")

class mysqLDB(DBinterface):
    def establishDB(self):
        print("mysql DB connection")
    def disconnectDB(self):
        print("mysql DB disconnection")
dbname=input("enter db name")
classname=globals()[dbname]
c=classname
c.establishDB()
c.disconnectDB()

#encapsulation:
    data binding

#with in the same and the inherited (child)classed

    * _  ---->protected variable

    * __ ---->private variable



class test:
    a=100
    _b=200
    __c=300
    def display(self):
        print(test.a)
        print(test._b)
        print(test.__c)
t=test()
t=display()
print(test.a)
print(test._b)
print(test.__c)


class test:
    a=100
    _b=200
    __c=300
    def __init__(self):
        self.__no=1234
    def display(self):
        print(test.a)
        print(test._b)
        print(test.__c)
t=test()
#t=display()
#print(test.a)
#print(test._b)
print(test.__c)
print(t.__test__ no)


