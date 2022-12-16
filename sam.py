#bigoftwo=lambda no1,no2 if no1>no2 else no2
#print(bigoftwo(10,20))
#
#bigoftwo=lambda no1,no2: if no1>no2 else no2
#print(bigoftwo)
#
#sumoftwo=lambda no1 no2: no1+no2
#print(sumoftwo)
#
#

#day 17

#recursion,lambda functions and modules

#recursion
#cursive writing
#recursive
#block of statements


#black of statments
    #for 
    #while
    #if
#function -name set of instructions

#recursion

def getusernamepassword(username,password):
    if username!='abcd':
        print("incorrect username")
        username=input("username :")
        password=input("password :")
        getusernamepassword(username,password)
    elif password!='abcd':
        print("incorrect password")
username=input("username :")
password=input("password :")
getusernamepassword(username,password)


def getusernamepassword(username,password):
    if username!='abcd':
        print("incorrect username")
        username=input("username :")
        password=input("password :")
        getusernamepassword(username,password)
    elif password!='abcd':
        print("incorrect username")
        username=input("username :")
        password=input("password :")
        getusernamepassword(username,password)
username=input("username :")
password=input("password :")
getusernamepassword(username,password)

def display(n):
    print(n)
display(1)

def display(n):
    print(n)
    n+=1
    if n<=5:
        display(n)
display(1)
#function called itself
#def not using loop function 
#no loops while ,for not use def
#if statment compalsayri

#problem

#addition of digits
#factorial
#gcd
#lcm
#fibonacci series


#functional def code

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
result=fact(4)
print(result)

def fact(num):
    if num==1:
        return 1
    else:
        return num+fact(num-1)
result=fact(5)
print(result)

#while loop

#12345
num=12345
total=0
while num>0:
    rem=num%10
    total=total+rem
    num=int(num/10)
print(total)

#recursion

def sumofdigits(num):
    if num==0:
        return 0
    else:
        rem=num%10
        no=int(num/10)
        return rem+sumofdigits(no)
print(sumofdigits(1873))

#def traiout
#palindrome
#armstrong
#reversea string
#reversea a sentence
#fibo
#gcd
#lcm

#anonymous functions:
#lambda function

def squareofnum(n):
    return n*n
print(squareofnum(10))


#lambda functions
#  filter
#  map
#  reduce

#nusted fumctions

def outer():
    print("i am standing in other function")
    def inner():
        print("i am standing inside inner function")
    print("outer to inner")
outer()

#key word variable length 
#lambda functions
#reursion
#modules
#group of functions,variable and classes

num=123
def add():
    return 10
def subtract():
    return 20
print(add())
print(subtract())

#calc.py

num=123
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide (a,b):
    return a/b
print(add(10,20))
print(subtract(10,20))

import calc
print(calc.num)
print(calc.add(1000,11111))

import calc as c
print(c.num)
print(c.add(1000,11111))
print(c.multiply(10,20))

from calc import *
print(add(1000,11111))
print(mutiply(10,20))

from calc import *
print(add(10,20))

#1 multiple modules
# import module 1 as m1 ,modules2 as m2
# import module 1,module2
# module member=variables,functions

from calc import num as no,add as sum
print(sum(1000,11111))
print(dir(calc))
print(dir())

import calc 
print(sum(1000,11111))
print(dir(calc))
print('bubble python program or not ',__name__)

#math module

import math 
print(dir(math))


from random import *

for i in range(10):
    print(random)
for i in range(10):
    print(randint(1,100))
for i in range(10):
    print(randrange(1,100,2))

