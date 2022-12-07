#day4

#greatest common divisors

no=3
count=10
while count>=1:
    print(no)
    no+3
    count-=1

no=int(input("enter no"))
count=int(input("how many times"))
while count>=1:
    print(no)
    no+3
    count-=1

# multiples of given number

#big=no1 if no1>no2 else no2
#  or
#if no1>no2:
    #big=no1
#elif no2>no1:
    #big=no2

no1=2
no2=8
big=no1 if no1>no2 else no2
if big %no1==0 and big%no2==0:
    print("least commom multiple is ",big)


no1=2
no2=9
big=no1 if no1>no2 else no2
if big %no1==0 and big%no2==0:
    print("least commom multiple is ",big)
big+=1
if big %no1==0 and big%no2==0:
    print("least commom multiple is ",big)
big+=1
if big %no1==0 and big%no2==0:
    print("least commom multiple is ",big)
big+=1

#least common multiple (lcm)

no1=int(input("enter no1 :"))
no2=int(input("enter no2 :"))
big=no1 if no1>no2 else no2
while True:
    if big %no1==0 and big%no2==0:
        print("least commom multiple is ",big)
        break
    big+=1

no1=int(input("enter no1 :"))
no2=int(input("enter no2 :"))
big=no1 if no1>no2 else no2
count=5
while True:
    if big %no1==0 and big%no2==0:
        print("least commom multiple is ",big)
        break
    big+=1
    count-=1

#factorial
#5!=5*4*3*2*1
no=int(input("enter no"))

#factorial

total=0
no=5
while no>1:
    total+=no
    no-=1
print(total)

total=0
no=5
while no>1:
    total*=no
    no-=1
print(total)

total=0
no=int(input("enter no"))
while no>1:
    total*=no
    no-=1
print(total)

#prime no programs

no=int(input("enter no"))
div=2
while div <no:
    if no%div==0:
        print('not prime')
        break
    div+=1
else:
    print('prime')

#reverse a number

no=input("enter no")
i=len(no)-1
while i>=0:
    print(no[i])
    i-=1
print(type(no))

#addition of digits  4+3+2+1==10

no=input("enter no")
sumofdigits=0
i=len(no)-1
while i>=0:
    print(no[i])
    #print(type(no[i]))
    sumofdigits=sumofdigits+int(no[i])
    i-=1
print(sumofdigits)

#sumofdigits

no=input("enter no")
sumofdigits=0
i=len(no)-1
while i>=0:
    print(no[i])
    #print(type(no[i]))
    sumofdigits=sumofdigits+int(no[i])
    i-=1
print(sumofdigits)

# palindrome program

no=input("enter no")
reverse=' '
print(reverse)
i=len(no)-1
while i>=0:
    reverse=reverse+no[i]
    i-=1
print(reverse)
if no==reverse:
    print('palindrome')
else:
    print('not palindrome')

no=int(input("enter no"))
count=0
while no>0:
    print(no%10)
    no=no//10
    count+=1
print('count of digits',count)

no=int(input("enter no"))
count=0
sumofdigits=0
while no>0:
    sumofdigits=sumofdigits+(no%10)

    print(no%10)
    no=no//10
    count+=1
print("addition of digits",sumofdigits)
print('count of digits',count)

no=int(input("enter no"))
count=0
sumofdigits=0
while no>0:
    sumofdigits=(sumofdigits*10)+(no%10)
    print(no%10)
    no=no//10
    count+=1
print('addidition of digits',sumofdigits)
print('count of digits',count)

no=int(input("enter no"))
no2=no
count=0
sumofdigits=0
while no>0:
    sumofdigits=(sumofdigits*10)+(no%10)
    print(no%10)
    no=no//10
    count+=1
print(no)
print('reverse value is',sumofdigits)
if no2==sumofdigits:
    print("palindrome")
print('count of digits',count)

# armstrong number 
#  153
#3-->3*3*3=27
#5-->5*5*5=125
#1-->1*1*1=1    
#27+125+1=153  this is armstrong number

no=153
no2=no
count=0
armstrong=0
while no>0:
    rem=no%10
    armstrong+=rem*rem*rem
    no=no//10
    count+=1
#print(no
#print('reverse value',sumofdigits))
if no2==armstrong:
    print("armstrong")

else:
    print("armstrong")

#try

#armstrong number
#neon number
#triangular number
#strong number
#perfect number

#fibonacci series

f,s=-1,1
count=int(input("enter range"))
while count>0:
    t=f+s
    print(t,end='')
    f=s
    s=t
    count-=1

f,s=-1,1
count=int(input("enter range"))
while count>0:
    t=f+s
    print(t,end='')
    if t==count:
        break
    f=s
    s=t
    count-=1

# fiboncci

first=-1
second=1
count=int(input("enter number"))
while count>0:
    print(first+second)
    second=first+second
    first=second-first
    count-=1


