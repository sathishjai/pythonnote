DAY 14
     DICTIONARY

*no dublicate keys allowed
*values-duplicate values allowed
*no insertion order
*dictionaries are mutable

#dictionary creation:

d={}
print(type(d))
d[1234]='celin'
d[1235]='ilangoven'
d[1236]='ilangoven'
d[key]='value'
*no dublicate keys allowed
*values-duplicate values allowed

d={1234:'celin',1235:'ilangovan',1236:'rajarajan',1237='lenin'}
print(d)
print(d[1234])
print(d[1235])
d[1236]='arvind'-----> (key value change)
print(d)
d=[100]='thas' ------>(new id adding)

remove function for dictionary

d={1234:'celin',1235:'ilangovan',1236:'rajarajan',1237='lenin'}
del d[1234]
print(d)

#clear()
#del d

d.clear()     ---->{} empty dictionary
print(d)

del d         ----->name error name'd' is not defined
print(d)                      (d) dictionary deleted

get function

d={1234:'celin',1235:'ilangovan',1236:'rajarajan',1237='lenin'}
print(len(d))
print(d.get(1234))      ----->'celin'
print(d.get(1235))      ----->output=none
print(d[1234])          ----->'celin'
print(d[12345])         ----->error

pop function

print(d.pop(1235))
print(d)
print(d.pop(12345))    ----->key error
d.pop(key)             ----->key=1234   ,value='celin'
print("beforee popitem",d)
print(d.popitem())
print("after popitem",d)

name=input("enter name")
roll no=int(input("enter roll no"))
d[roll no]=name

#d={1234:[78,89,98,100],1235:[90,80,70,78],1236:[100,98,45,87]}
d={1234:['celin','abcd','xyz',40]}
print(d)

d={1234:['celin',('abcd',True),'xyz',40]}
print(d)

d={1234:'celin',1235:'ilangovan',1236:'rajarajan',1237='lenin'}
print(d.keys())
print(type(d.keys())
for key in d.keys():
	print(key)

d={1234:'celin',1235:'ilangovan',1236:'rajarajan',1237='lenin'}
print(d.values())
print(type(d.values())
for value in d.values():
	print(value)

d={1234:'celin',1235:'ilangovan',1236:'rajarajan',1237='lenin'}
for item in items():
	print(item)
	print(type(item))

#d1=d.copy()
#d1.update(d)

d={'name':'kathiravan','age':50}
print(d.get('name'))     ----->'kathiravan'
print(d.get('salary'))   ----->none
print(d.get(salary',0))  ----->0
print(d.get(salary','not available')  ----->'not available'

d=eval(input("enter dictionary"))
print(d)

#geting items for dictionary at run time

register={}
no=int(input("enter no of students"))
i=0
while i<no:
	name=input("enter name")
	mark=int(input("enter mark"))
	register[name]=mark

register={}
while True:
	name=input("enter name")
	mark=int(input("enter mark"))
	register[name]=mark
	nextcandidate=input("enter no to stop")
	if nextcandidate=='no':
		break


register={}
total=0
while True:
	name=input("enter name")
	mark=int(input("enter mark"))
	register[name]=mark
	nextcandidate=input("enter no to stop")
	if nextcandidate=='no':
		break
print(total)

prices={'apple':100,'grapes':200,'banana':50,'orange':60}
for prodname,prodprice in price.item():
	print(prodname:'----->',prodprice)
for x in prices.items():
	print(x)

prices={'apple':100,'grapes':200,'banana':50,'orange':60}
for prodname,prodprice in price.item():
	print(prices[prodname])

prices={'apple':100,'grapes':200,'banana':50,'orange':60}
print(prices)
for prodname,prodprice in price.item():
	prices[prodename]=prices[prodname]-10

#10% discount code

prices={'apple':100,'grapes':200,'banana':50,'orange':60}
print(prices)
for prodname,prodprice in price.item():
	prices[prodename]=prices[prodname]-prices[prodname]//10
print(prices)

#'grapes' remove function code

prices={'apple':100,'grapes':200,'banana':50,'orange':60}
print(prices.keys())
for name in price.item():
	print(name)
	print(price)
     (OR)
prices={'apple':100,'grapes':200,'banana':50,'orange':60}
print(prices.keys())
l=prices.keys()
for x in l():
	if x=='grapes':
		del prices[x]
		break
print(prices)

#big projects using dictionary function:

*values()
*keys()
*get()
*items()
 
very very importent 
*d[1234]--->'celin'
*d[key]---->'value
value printed


