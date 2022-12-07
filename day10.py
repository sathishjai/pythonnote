#list introduction

s1=input("enter 1st string numbers : ")
s2=input("enter 2nd string numbers : ")

comb=''
if len(s1)<len(s2):
    i=0
    for i in range(4):
        comb+=s1[i]+s2[i]
    i+=1
print(i)
comb=comb+s2[i:]
print(comb)

s1=input('enter nsme :')
s2=input('enter nsme :')
if len(s1)<len(s2):
    l=len(s1)
elif len (s2)<len(s1):
    l=len(s2)
output=''
i=0
while i<l:
    output=output+s1[i]
    output=output+s2[i]
    i+=1
print(output)


s1=input("enter 1st string numbers : ")
s2=input("enter 2nd string numbers : ")
comb=''
i,j=0,0
while i<len(s1) or j<len(s2):
    if i<len(s1):
        comb=comb+s1[i]
        i+=1
    if j<len(s2):
        comb=comb+s2[j]
        j+=1
print(comb)

s1=input("enter 1st string  : ")
s2=input("enter 2nd string  : ")
comb=' '
i,j=0,0
length=len(s1)
length2=len(s2)
print(i)
print(j)
print(length)
print(length2)
while i<length or j<length2:
    if i<len(s1):
        comb=comb+s1[i]
        i+=1
    if j<len(s2):
        comb=comb+s2[j]
        j+=1
print(comb)


s1=input("enter 1st string  : ")
s2=input("enter 2nd string  : ")
comb=' '
if len(s1)<len(s2):
    for i in range(len(s1)):
        comb=comb+s1[i]+s2[i]
        i+=1
    for x in range (i,len(s2)):
        comb+=s2[x]
        x+=1
    print('merged string is : ',comb)
else:
    for i in range (len(s2)):
        comb=comb+s1[i]+s2[i]
        i+=1
    for x in range(i,len(s1)):
        comb+=s1[x]
    print('merged string is :',comb)


s1='A5B6C7'
output=''
for letter in s1:
    if letter.isalpha():
        output+=letter
for letter in s1:
    if letter .isdigit():
        output+=letter
print(output)

s1='A5B6C7'
output1=''
output2=''
for letter in s1:
    if letter .isalpha():
        output1+=letter
    else:
        output2+=letter
print(output1)
print(output2)
output=output1+output2
print(output)

name='ram'
print(name*3)

s=input("enter value :")
output=''
output=output+s[0]
output=output*int(s[1])
print(id(output))
print(output)

s=input("enter value :")
output=''
i=0
while i<len(s):
    output=output+s[i]
    output=output*int(s[i+1])
    i+=2
print(output)

#compound data types:
#list:
    #list of objects
#grocery list:
    #gorup of object into a single entity
#--->insertion objects into a single entity
#duplicate object is maintained
#heterogenous objects are allowed 
#list object are mutable

#list creation 
grocerylist=[]

marklist=[100,98,45,36]
print(marklist)

name='stephen'
l=list(name)
print(l)

l2=list(range(5))
print(l2)

name='stephen'
l=list(name)
print(l)
name2=str(l)
print(name2)
print(type(name2))
print(name2[0])
print(name2[1])
print(name2[2])

sentence='Happy New Year'
list=sentence.split()
print(list)

sentence="best bike with good milage in india"
list=sentence.split()
for x in list:
    print(x)

l=[10,20,'a',True]
print(l[3:0:-1])
print(l[1])
print(l[2])
l[0]=777
print(l)

l=[10,20,'a',True]
for x in l:
    print(x)

l=[10,20,30,40,50,60,70,80,90,100]
for x in l:
    if x%20==0:
        print(x)

l=10,20,'a',True
i=0
while i<len(l):
    print(l[i])
    i+=1

#list is a datatype -True /False
#list can contain heterogeneous objects-True/False
#list can contain any datatype -True /False

#list is a datatype -True /False

l1=[10,20,30,40,50,60,70,80,90,100]
l2=['a','b','c']
l3=l1+l2
print(l3)
print(type(l3))
print(len(l3))

ll=[l1,l2]
print(len(ll))
print(ll)
print(ll[0])
print(len(ll[0]))
print(len(ll[1]))

l1=[10,20,30,40,50,60,70,80,90,100]
l2=['a','b','c']
l3=l1+l2
ll=[l1,l2]
print(l[0])
print(ll[1])
print(ll[0][0])
print(ll[1][0])

l3=l1+l2
ll=[l1,l2]
for x in ll:
    print(x)


outerlist=[l1,l2]
for innerlist in outerlist:
    for element in innerlist:
        print(element,end='')
    print()


outerlist=[l1,l2]
for innerlist in outerlist:
    for element in outerlist:
        print(element,':',type(element),end='')
    print()

for innerlist in outerlist:
    for element in innerlist:
        if type(element)==int:
            print(element,end='')
    print()

for innerlist in outerlist:
    for element in innerlist:
        if element==40:
            element='abc'
            print(element,end='')
    print()


