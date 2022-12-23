 OBJECT ORIENTED PROGRAMMING -CONTRUCTOR -INHERITANCE

import sys 
class customer:
    '''this is customer of indian bank'''
    bank='indian overseas bank'
    def deposit(self,amount):
        pass 
    def withdraw(self,amount):
        pass
print('welcome to ',customer.bank name)
name=input('what is your name?')
accno=int(input("enter your account no"))
customer1=customer(name,accno)


import sys 
class customer:
    '''this is customer of indian bank'''
    bank='indian overseas bank'
    def deposit(self,amount):
        name=input('what is your name?')
        accno=int(input("enter your account no"))
    def withdraw(self,amount):
        name=input('what is your name?')
        accno=int(input("enter your account no"))


import sys 
class customer:
    '''this is customer of indian bank'''
    bankname='indian overseas bank'
    def __init__(self,name,accountno):
        self.name=name
        self.accno=accountno
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balanceofamount
        print(self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print('insufficient balance')
        else:
            self.balance=self.balance-amount
            print(self.balance)
print('welcome to ',customer.bank name)
name=input('what is your name?')
accno=int(input("enter your account no"))
customer1=customer(name,accno)

while True:
    print('enter your choice')
    print('d-Doposit','w-Withdraw','s-Stop')
    choice=input('enter your choice')
    if choice=='d':
        amount=int(input('enter amount'))
        customer1.deposit(amount)
        print(self.balance)
    elif choice=='w':
        amount=int(input('enter amount'))
        customer1.withdraw
        print(self.balance)
    elif choice=='s':
        sys.exit()


