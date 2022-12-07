
#string function and programs

#string is immutable
#find()
#rfind()
#index()
#rindex()

s='python'
print(s.find('y'))

s='python is easy'
print(s.rfind('y'))

s='python is easy'
print(s.rfind('y',5,14))

s='python is very easy'
position=-1
length=len(s)
position=s.find('y',0,length)
print(position)
position=s.find('y',position+1,length)
print(position)
position=s.find('y',position+1,length)
print(position)
position=s.find('y',position+1,length)
print(position)

s='python is very very easy'
position=-1
length=len(s)
while True:
    position=s.find('y',position+1,length)
    if position==-1:
        break
    print('y is present at',position)

s='python is very very easy'
position=-1
length=len(s)
count=0
while True:
    position=s.find('very',position+1,length)
    if position==-1:
        break
    print('very is present at',position)
    count+=1
print(count)

s='python is very very easy'
position=-1
length=len(s)
sticker=False
count=0
while True:
    position=s.find('b',position+1,length)
    if position==-1:
        break
    count+=1
    print('b is present at',position)
    sticker=True
print(count)
if sticker==False:
    print('b is not present at all')

s='python is very very easy'
finds=input("search letter :")
position=-1
length=len(s)
sticker=False
count=0
while True:
    position=s.find(finds,position+1,length)
    if position==-1:
        break
    count+=1
    print(finds, 'is present at',position)
    sticker=True
print(count)
if sticker==False:
    print(finds,'is not present at all')

s='python is very very easy'
position=-1
length=len(s)
sticker=False
count=0
while True:
    position=s.find('y',position+1,length)
    if position==-1:
        break
    count+=1
    print('y is present at',position)
if count==0:
    print('y is not present at',position)
else:
    print('y is present',count,'times')

s='python is very very easy'
print(s.count('b'))

s='python is very very easy'
print(s.count('y'))


s='python is very very easy'
count=0
for x in s:
    if x=='y':
        count+=1
else:
    print(count)

s='python is very very easy'
count=0
position=0
for x in s:
    if x=='y':
        print(x,'is present at',position)
        count+=1
    position+=1
else:
    print(count)

s='python is very very easy'
position=0
for x in s:
    if x=='y':
        print(x,'is present at',position)
    position+=1

s='python is very very easy'
print(s.count('y',14,24))
print(s.count('y',5,24))

s='python is very very easy'
length=len(s)
print(s.count('y',5,length))

s='raja'
s2=s.replace('r','k')
print(s2)

s='you can not do'
s2=s.replace('not','')
print(s2)

s='python is easy'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
print(s.capitalize())

#number---->iteration
#iteration--->looping
#looping---->while,for
#condition
#length

mail_id=input("enter your mail id")
i=0
while i<len(mail_id):
    if mail_id[i]>='0'and mail_id[i]<='9':
        print(mail_id[i],end='')
    i+=1


mailid=input("enter your mailid")
i=0
for x in mailid:
    if x>='0'and x<='9':
        print(x)
    i+=1

mail_id=input("enter your mail id")
i=0
while i<len(mail_id):
    if mail_id[i]>='a'and mail_id[i]<='z':
        print(mail_id[i],end='')
    i+=1


mail_id=input("enter your mail id")
i=0
while i<len(mail_id):
    if not mail_id[i]>='a'and mail_id[i]<='z':
        print(mail_id[i],end='')
    i+=1

mailid=input("enter your mail id")
i=0
while i<len(mailid):
    if not mailid[i]>='a'and mailid[i]<='z':
        if not mailid[i]>='0'and mailid[i]<='9':
            print(mailid[i],end='')
    i+=1

s='python is very'
print(s.startswith('python'))
print(s.endswith('python'))
print(s.isalpha())
print(s.isdigit())

mobile=(input("enter mobile number"))
for letter in mobile:
    if not(letter>='0' and letter<='9'):
        print('not correct mobile number')
        break
else:
    print("correct mobile number")

name=input('enter your name all in black letters')
for letter in name:
    print(letter,end=' ')


name=input('enter your name all in black letters')
for letter in name:
    if not letter >='a' and letter<='z':
        print("no.not all letters are capitals")
        break
else:
    print("yes.perfect")

#mobile number validation

name=input("enter your name-all in black letters")
for letter in name:
    if not (letter>='a' and letter<='z'):
        print("no.not all letter are capital")
        break
else:
    print("yes perfect")

#all letter are small or not

name=input("enter your name -all in black letter")
print(name.islower())
print(name.isupper())
print(name.istitle())
print('python Is Easy'.istitle())
print('python Is Easy'.isspace())

#count of space in a given sentence

s=input("enter a sentence")
space_count=0
for x in s:
    if x==' ':
        space_count+=1
else:
    print(space_count)

name='raja'
salory=20000
age=55
print(name,salory,age)
print("{}is his name,his salory is {} and his age is {}" .format(name,salory,age))
print("{0}is his name,his salory is {1} and his age is {2}" .format(name,salory,age))
print("{}is his name,his salory is {} and his age is {}" .format(name,salory,age))

#merging letter form tow words alternatively

s1='pto'
s2='yhn'
output=''
i=0
while i<len(s1):
    output=output+s1[i]
    output=output+s2[i]
    i+=1
else:
    print(outp-ut)

