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


