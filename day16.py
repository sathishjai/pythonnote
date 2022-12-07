DAY 16
Function ,type of Arguments Variable.
Function
*print()
*id()
*round()
*input()
*eval()
*items()
*keys()
*values()

def wish(greetings):
	print(greeting)
wish(“happy Thursday”)

def wish(name):
	print(‘hi’)
	print(name)
	print(“welcome to python class”)
count=1
while count<=50:
	name=input(“enter your name”)
	wish(name)
	count+=1

def wish():
	print(‘hi’)
	print(“welcome to python class”)
wish()
wish()
wish()

def squarofnumber(num):
return mum*num
result=squerofnumber(5)
print(result)

def add(no1,no2):
	return no1+no2
result=add(10,20)
print(result)

def add(no1,no2):
	return no1+no2           
print(result)

def add (no1,no2):
	print(‘hi’)
	#return no1+no2           #output=hi none  
print(add(10,20))  
                                     
def add (no1,no2):
	print(‘hi’)
	return no1+no2           #output=hi 30  
print(add(10,20))                                       

def add (no1,no2):
	print(‘hi’)
	#return n o1+no2           
print(type(add(10,20)))

def add (no1,no2):
	print(no1+n02))
	return n o1+no2   
print(add(10,20)        
print(type(add(10,20)) 
       
def odd_even(no):
	if no%2==0:
		print(‘even’)
	else:
		print(‘odd’)
num=int(input(“enter no:”))
odd_even(num)    
                           
def odd_even(no):
	if no%2==0:
		print(‘even’)
	else:
		print(‘odd’)
for num I range(1,5):
    odd_even(num)

def calculate(no1,no2):
	add=no1+no2
	sub=no1-no2
	mul=no1*no2
div=no1//no2
return add,sub,mul,div
print(calculate(100,50))

def calculate(no1,no2):
	add=no1+no2
	sub=no1-no2
	mul=no1*no2
div=no1//no2
return add,sub,mul,div
result=calculate(100,50)
for x in result:
	print(x)

#type of arguments:
wish(name):
	print(name)
wish(‘sibi’)

#four type of arguments
#1 positional arguments
#2 keyword arguments
#3 default arguments
#4 variable arguments

1 positional arguments
def add(no1,no2):
	return no1+no2
add(100,50)


2 keyword arguments
def wish(name,msg):
	print(‘hi’,name,msg)
wish(‘ganesh’,’welcome’)
wish(name=‘ganesh’,msg=’welcome’)
wish(msg=’welcome’ ,name=‘ganesh’)
wish(name=‘ganesh’,’welcome’)
wish(‘ganesh’,msg=’welcome’)     output=error

3 default arguments
def wish(name=’admin’):
	print(‘hi’,name)
wish(‘aishwarya’)
wish(‘admin’)

4 variable arguments
def calculatetotal(*n):
	total=0
for subject in n:
	total=total+subject
print(total)
calculatetotal(90)
calculate(90,80,70)
calculate()
def calculatetotal(**kwargs):
	for sub,mark in kwargs.items():
		print(sub,”scored”,mark)
		print(sub,”scored”,mark)
calculatetotal(tamil=90)
calculatetotal(tamil=90,english=80,maths=70)
calculatetotal(tamil=90,english=80,maths=’seventuy’)
calculatetotal(tamil=90,english=’DNA’,maths=false)

#two types of variable.
	#global variable
	#local variable

#function -group of instructions with a name
#module-group of function saved to a file
#library -group of modules

#global variable
discount=20
def purchaseTV():
    print(diacount)
def purchaselaptop():
    discount=25
    print(discount)
purchaseTV()
purchaselaptop()

dis count=20
def opening time():
    global discount
    discount=30
    print('of',discount)
def purchaseTV():
    print(discount)
def purchaselaptop():
    discount=25
    print(discount)
opening time(
purchaseTV())
purchaselaptop()

def purchaselaptop():
    discount=25
    print(globals())['discount']
    print(discount)


