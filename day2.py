# day2

# assiginment operators

no1=100
no1+=10

no=5
no=no+1
no-=2
#assignment operators

no*=1
no/=1
no//=1
no%=1
#no&=1
#no|=1
#no^=1
#no<<=1
#no>>=1

#input function

name=input("enter value")
print(type(name))

#dynamically typed programming language
#type --->datatype

num=input("tell me any no .")
num2=input("tell me anouther no .")
#type casting
num=int(num)
num2=int(num2)
print("total is ", num+num2)

#eval function

result=eval("10+20+30")
print(result)

exp=input("enter any arithmatic expression :")
result2=eval(exp)
print(result2)


#module, --package, --folder, --files,functions,variable

#input()
#print()
#eval()
#int()

#pi=3.14
#sin(30)

#command line arguments
#folder-modules
#add()--mathematical
#add()--sin(45)+cos(45)
import math
print(math.pi)

#output function

a,b,c=100,200,300
print(a,b,c, sep=':')
print(a,b,c ,end='-')

#formatted string
# %i-->int
# %d-->int
# %f-->float
# %s-->string

a,b,c=100,200,300
print('a value %d'%a)
print("b value is %d and c is %d"%(b,c))

name='langscape'
print('welcome to %s' %name)

#replacement operator

name='ganesh pandian'
city='chennai'
print('hi this is {0}.i am from{1}'.format(name,city))
#{0}{1}replacement operators

print("hi this is {0}. i am from{1}".format(city,name))
print("hi this is {1}. i am from{0}".format(city,name))
print("hi this is {}. i am from{}".format(city,name))

#medel operators

name=input("enter your name ")
print(len(name))
mid=len(name)//2
print(name[:mid]+name[mid].upper()+name[mid+1:])
#print(name[0:4]+name[4].upper()+name[5:])

#name=input("enter your name")
#name[0]=name[0].upper()
#print(name)

#control flow statments

mark=90
if mark>=90:
    print("very good")
else:
    print("good")

name=input("name pleace:")
if name=='muthu':
    print('glad to meet you ')
print('hello')

mark=int(input("enter mark :"))
if mark>90:
    print('90+')
elif mark>80:
    print('80+')
elif mark>70:
    print('70+')
else:
    print('we are in same boat')

mark1=int(input("enter your 10th mark "))
mark2=int(input("enter your 10th mark "))
if mark1>mark2:
    print('first person')
elif mark2>mark1:
    print('second person')
else:
    print('both got same marks')


#nested if statment
total=int(input("enter total "))
if total>400:
    tamil=int(input("enter tamil mark"))
    if tamil>80:
        print("very good")
    else:
        print("nice")
else:
    print("ok thanks")

total=int(input("enter total "))
if total>500:
    print("sorry enter upto 500")
    total=int(input("enter total "))
    if total>400:
        tamil=int(input("enter tamil mark"))
        if tamil>80:
            print("very good")
        else:
            print("nice")
else:
    print("ok thanks")

#iterative statments

#   while 
#   for

mind=43
#until your guess and mind value same ,contince below steps
#stop executing below steps when your guess and mid valu are same
guess=0
while guess!=mind:
    guess=int(input("tell me your guess"))
    if guess==mind:
        print('wow,supper')
    elif guess>mind:
        print("no,your guess is greater")
    else:
        print("no,too little")

