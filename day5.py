# day 5
# decimal to binary

no=int(input("enter no "))
binary=''
while no>0:
    rem=no%2
    binary=str(rem)+binary
    print(rem)
    no=no//2

# decimal to binary

no=int(input("enter no "))
binary=''
while no>0:
    rem=no%2
    binary=str(rem)+binary
    #print(rem,end='')
    no=no//2
else:
    print(binary)

#modules=file/folder
# code reusability
#abstraction-->showing only necessary data and hiding unwanted one

import math
no=int(input("enter num "))
power=int(input("enter power"))
print((math.pow(no,power)))

#binary of decimal

import math
no=int(input("enter binary"))
decimal=0
i=0
while no>0:
    rem=no%10
    value=rem*int(math.pow(2,i))
    decimal+=value
    no=no//10
    i+=1
else:
    print(decimal)

