# day3
#iterative statments:
#1, what 
#2, how many

count=0
while count<5:
    print(1)
    count=count+1

count=0
while count<5:
    print(count)
    count=count+1

# what should be printed
# what is the initial value?
# what pattern you are observing
# what is the final value
 #    ( this 4 contition is very importent)

count=5
while count>=1:
    print(count)
    count=count-1

count=10
while count>=1:
    print(count)
    count=count-2

count=2
while count<=10:
    print(count)
    count=count+2

count=2
while count<=100:
    print(count,sep=' ')
    count=count+2

count=1
while count<=10:
    print(count,sep=' ')
    count=count+2

count=1
maxno=int(input("enter maximum number"))
while count<=maxno:
    print(count,sep=' ')
    count+=2

count=3
maxno=int(input("enter maximum number"))
while count<=maxno:
    print(count,sep=' ')
    count+=3

count=3
maxno=int(input("enter maximum number"))
while count<=maxno:
    print(count,sep=' ')
    count*=3

start=1
while start<=20:
    if start%3==0:
        print(start)  #(this code 20 time run speed slow vaa erukum)
    start+=1

start=3
while start<=20:
    print(start)  #(best code only 6 time run tish code)
    start+=1

start=1
while start<=20:
    if start%3==0 and start % 2==0:
        print(start)
    start+=1

start=1
while start<=100:
    if start%3==0 or start % 2==0:
        print(start)
    start+=1

amount=1
days=5
box=0
while amount <=days:
    box=box+amount
    amount+=1
print(box)


amount=1
days=int(input("enter max range"))
bo=0
while amount <=days:
    box=box+amount
    amount+=1
print(box)

name=input("what is your name?")
length=(len(name))
i=0
while i<length:
    print(name[i])
    i=i+1

#what is to be printed    (i=index)
#starting point
#ending point
#pattern

name=input("what is your name?")
length=len(name)
i=0
while i<length:
    if name[i]=='a':
        print(name)
        break
    i+=1

name=input("what is your name?")
length=len(name)
i=0
while i<length:
    if name[i]=='a':
        i+=1
        continue
    print(name[i])
    i+=1

no=0
while no<10:
    no+=1
    if no==5:
        break
    print(no)

no=0
while no<10:
    no+=1
    if no==5:
        continue
    print(no)

# vowels count

name=input("what is your name?")
length=len(name)
i=0
while i<length:
    if name[i] in ['a','e','i','o','u']:
        print(name[i])
    i+=1
#    if name[i] not in ['a','e','i','o','u']

name=input("what is your name?")
length=len(name)
i=0
count=0
while i<length:
    if name[i] in ['a','e','i','o','u']:
        count+=1
        print(name[i])
    i+=1
print("no of vowels prosent are ",count)


#words count

name='chennai tamil nadu'
length=len(name)
i=0
count=1
while i<length:
    if name[i] ==' ':
        count+=1
    i+=1
print(count)


