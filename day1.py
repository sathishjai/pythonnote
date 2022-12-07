#escape characters
 
print("hi hello")
print("hi\thello")
print("hi\nhello")
print("hi\hello")
print('i\'m muthuramalingam')

#operators
#arithmatic operators
# + - * / % // **

print(5+10)
print(10-5)
print(10*5)
print(10/5)
print(10//5)
print(10/3)
print(10//3)
print(10%3)
print(10%4)
print(10**2)
print(10**3)
print(3**2)

#relation operators
#> >= < <= 

print(10>5)
print(5>10)
print(100>=100)
print(100>99)
print(100>100)
print(200<100)
print(200<200)
print(200<=500)

name1='abcde'
name2='abcdef'
print(name1>name2)

name1='abcde'
name2='abcd'
print(name1>name2)

name1='abcd'
name2='abcde'
print(name1>name2)

name1='pqrst'
name2='abcde'
print(name1>name2)

name1='abcde'
name2='pqrst'
print(name1>name2)

#chaining of operators

print(10<20<30)
print(10<20>15)
print(10<20>30)

#equality operators
# ==  !=
print(10==20)
print(10!=20)
print(10==20==100)
print(10!=20!=100)

#logic operators

#and  or  not

a=False
b=not a
print(a)

print(0 and 5)
print(1 and 5)
print(5 and 1)
print(0 and 0)
print(0 or 5)
print(1 or 5)
print(5 or 1)
print(0 or 0)

#bitwise operators
# & | ^ ~ << >>
# binary digits---> 0,1

#member ship operators

sentence="channai b=is the capital of tamil nadu"
print('chennai' in sentence)
print('chennai' not in sentence)

subjects=['tamil','english','maths','science']
print('social ' in subjects)

#ternary operators  --> conditional operators

a,b=10,20
c=30 if a>b else 40
print(c)

a,B=100,20
c=30 if a>b else 40 
print(c)

a=100 #a=1000 #a=1000
b=200 #b=200  #b=2000
c=300 #c=300  #c=300
min=a if a<b and a<c else b if b<c else c
print(min)

a=100 #a=1000 #a=1000 #a=1000
b=200 #b=200 #b=2000 #b=2000
c=300 #c=300 #c=300 #c=300 #c=3000

max=a if a>b and a>c else b if b>c else c
print(max)

#identity operators
# is isnot 

a=10 
b=10
print(a==b) #content comparator
print(a is b) #memory address comparator

# input function

name=input("enter your name")
print("hi",name ,"welcome to python world")
print("hi"+name+"welcome to python world")

#  , one space create two words center place
#  +  no space creat two words continuesly words printed


