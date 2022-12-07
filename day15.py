DAY 15
       DICTIONARY PROGRAMS.
employees={'kathiravan':100,'viyan':101,'navilan':102,'arul':103}
employees2={}
for name,no in emplyees.items():
	#print(name,':',no)
	employees[no]=name
print(employees)

e={"thulasi":key for key,value in e.items()}
print(e)
e={value:key for key,value in e.items()}
print(e)


employees={'kathiravan':25000,'viyan':30000,'navilan':40000,'arul':18000}
for name,salary in emplyees.items():
	if salary>25000:
		print(name,'salary is',salary)


name_list=[]
for name in emplyees.keys():
	name_list.append(name)
print(name_list)


salarylist=[]
for name in emplyees.values():
	salarylist.append(name)
print(salarylist)

#sorted  =ascending/descending
for name in sarted(employees):
	print(name.employees.values()):
for name in sarted(employees.values()):
	print(salary)

#sorting programs
l=[10,5,8,3]
print('before.sorting',l)
i=0
while i<len(l)-1:
	if l[i]>l[i+1]:
		l[i],l[i+1]=l[i+1],l[i]
	i+=1
print('afeter sorting',l)
i=0
while i<len(l)-2:
	if l[i]>l[i+1]:
		l[i],l[i+1]=l[i+1],l[i]
	i+=1
print('afeter sorting',l)
i=0
while i<len(l)-3:
	if l[i]>l[i+1]:
		l[i],l[i+1]=l[i+1],l[i]
	i+=1
print('afeter sorting',l)

#nested looping bubble sorting
l=[10,5,8,3]
j=1
while j<len(l):
	i=0
	while i<len(l)-j:
		if l[i]>l[i+1]:
			l[i],l[i+1]=l[i+1],l[i]
		i+=1
	j+=1
print('after sorting',l)

#bubble sorting for looping

def sorted():
l=[10,5,8,3]
print('before sorting',l)
n=len(l)-1
for j in range(0,n):
	for i in range(0,n):
		if l[i]>l[i+1]:
			l[i],l[i+1]=l[i+1],l[i]
	n=n-1
print('after sorting'l]

#linear search:
l=[10,20,30,40,5,8,3]
no=40
for x in l:
	if no==x:
		print('no is present')
		break
else:
	print('no is not present')

#binary search
#suitable for sorted set of elements

l=[10,20,30,40,50,60,70,80,90]
key=int(input("enter key to search")
min=0
max=len(l)-1
while min<=max:
	avg=(min+max)//2
	if key=l[avg]:
		print("key is present at",avg)
		break
	elif key>l[avg]:
		min=avg+1
	else:
		max=avg-1
else:
	print('key is not present')

d={'name':'kathiravan','age':50}
print(d.get('name')
print(d.get('age')
print(d.get('salary',0))
