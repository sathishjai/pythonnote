#(len,count,index,append,insert,extend)
no=65
print(chr(65))

no=1
no=no+64
print(chr(no))

no=5
no=no+64
print(chr(no))

no='a5'
print(no[0])
print(no[1])

no2=int(no[1])+65
print(chr(no2))

#list
    #dublicate elements are allowed
    #insertion order maintened

#[]
#[1,2,3]
#range()
#str

list=[10,20,30,40,50,10,20,30]
count=0
for x in list:
    if x ==20:
        count+=1
print(count)

list=[10,20,30,40,50,10,20,30]
prtnt(list.count(50))
print(list.index(30))

#manipulation of list function
# append()
 
list.append(500)
print(list)

nos=[]
for no in range(1,6):
    nos.append(no)
print(nos)

nos=[]
for no in range(1,11):
    if no %2==0:
print(nos)

l=[10,20,30,40]
l.append('kathir')
print(l)

l=[10,20,30,40]
l.insert(3,100)
l.insert(100,1000)
print(l)
l.insert(-100,3)
print(l)
l.insert(-90,4)
print(l)

# extend()

l1=['a','b','c']
l2=[1,2,3]
l1.extend(l2)
print(l1)
l1.extend('kathir')
print(l1)

#remove()

l=[10,20,30,40]
l.remove(10)
print(l)

#pop()
l=[10,20,30,40]
l.pop()
print(l)

l=[10,20,30,40]
l.pop(1)
print(l)

#stack--->first in last out
#queue--->first in first out

l=[10,20,30,40]
l.reverse()
print(l)

#reverse

l=['a','b','c','d']
i=len(l)-1
while i>=0:
    print(l[i],end='')
    i-=1

l=['a','b','c','d']
l2=[]
i=len(l)-1
while i>=0:
    l2.append(l[i])
    i-=1
print(l2)

#get a sentencefrom user
#convert that into a list l1
#reverse the list l1 and store in another list l2
#print list l2

sen=input("enter a sentence")
l=sen.split()
print(l)
l2=[]
i=len(l-1
while i>=0:
    l2.append(l[i
    i-=1
print(l2)

sen=input("enter a sentence")
l=sen.split()
print(l)
l2=[]
i=0
while i<len(l):
    l2.append (l[i])
    i+=2
print(l2)

sen=input("enter a sentence")
l=sen.split()
print(l)
l2=[]
i=0
while i<len(l):
    l2.append (l[i])[::-1]
    i+=2
print(l2)


sen=input("enter a sentence")
l=sen.split()
print(l)
l2=[]
i=0
while i<len(l):
    if i%2==0:
        l2.append(l[i][::-1])
    else:
        l2.append(l[i])
    i+=1
print(l2)

sen=input("enter a sentence")
l=sen.split()
print(l)
l2=[]
i=0
while i<len(l):
    if i%2==0:
        l2.append(l[i][::-1])
    else:
        l2.append(l[i])
    i+=1
print(l2)
output=''.join(l2)
print(output)

#input =sun mon tues wednes thurs fri satur 
#output=sunday monday tuesday wednesday thuresday friday saturday

input1 ='sun mon tues wednes thurs fri satur'
words=input1.split()
for word in words:
    print(word+'day')

input1 ='sun mon tues wednes thurs fri satur'
words=input1.split()
words2=[]
for word in words:
    words2.append(word+'day')
output=' '.join(words2)
print(output)


