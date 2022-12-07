# while loop for loop programs

#to every elements presnt in sequence
 #sequence=variable
 #elements=i
 #number sequence=range(3)

for no in range(100,121):
    print(no,end='')

for no in range(5,51,3):
    print(no,end='')

for no in range(51,5):
    print(no,end='')
else:
    print('xyz')

for no in range(51,5,-3):
    print(no,end='')
else:
    print('abcd')
    

for no in range(50,5,-3):
    print(no,end='')
else:
    print('abcd')

for x in [0,1,2]:
    print("hello")
    print(x)

#addition of first n numbers

total=0
for no in range(1,10):
    total=total+no
    print(no)
print(total)

total=0
value=int(input("enter no :"))
for no in range(1,value+1):
    total=total+10
    print(no)
print(total)

# factorial

total=1
value=int(input("enter no :"))
for no in range(1,value+1):
    total=total*no
print(total)

#no of words presents in a sentence

sentence='total is wednesday'
wordscount=1
for letter in sentence:
    if letter==' ':
        wordscount+=1
else:
    print('no of words',wordscount)

#prime number

no=int(input("enter no :"))
if no==2:
    print("prime")
elif no%2==0:
    print("not prime")
else:
    for i in range(2,no):
        if no%i==0:
            print('not prime')
            break
    else:
        print('prime')


word='sibi'
print(word)
count=len(word)
for i in range(count):
    print(i)

word='sibi'
count=len(word)
for i in range(0,count):
    print(word[i])

word='sibi'
count=len(word)
for i in range(3,-1,-1):
    print(word[i])

word='aishwarya'
print(word[::-1])

word='aiswarya'
print(word[::-2])

word=input("enter any word")
word2=word[::-1]
print(word2)
if word==word2:
    print("palindrome")
else:
    print("not palindrome")

#fibonacci series

f,s=-1,1
terms=int(input("enter terms"))
for i in range(terms+1):
    t=f+s
    print(t)
    f=s
    s=t

#nested loop

row=1
while row<=3:
    col=1
    while col<=5:
        print(col,end=' '')
        col+=1
    row+=1

row=1
while row<=3:
    col=1
    while col<5:
        print(col,end=' '')
        col+=1
    print()
    row+=1

row=1
while row<5:
    col=1
    print(row,":")
    while col<=row:
        print((row+col),end=' ')
        col+=1
    print()
    row+=1


