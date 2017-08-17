'''#1 random float number 10 to 100
import random
b=random.uniform(10,101)
print(b)

#2 float number 5 to 95
import random
b=random.uniform(5,96)
print(b)


#3 random even number 1 to 10
import random
b=random.randrange(0,11,2)
print(b)



#7 random divisible by 5 and 7 between 1 to 10

import random 
l=[]
l1=[]
for i in range(1,1001):
	if(i%5==0 and i%7==0):
		l.append(i)
print(l)
for j in range(0,5):
	a=random.choice(l)
	l1.append(a)
print(l1)

#5 random 5 numbers from 100 to 200

import random
b=[random.randint(100,201) for i in range(0,5)]
print(b)


#6 random 5 even number list from 100 to 200
import random
l=[]
l1=[]
for i in range(100,201):
	if(i%2==0):
 		l.append(i)
print("random even list",l)
for j in range(0,5):
	a=random.choice(l)
	l1.append(a)
print("random 5 choice number",l1)


#8 randomly print number from 7 to 15

import random
a=random.randint(7,16)
print(a)

#9 shuffle and print list [3,6,7,8]

import random
l=[3,6,7,8]
random.shuffle(l)
print(l)


#11 print list after remove even number
l=[5,6,77,22,14,12]
a=list(filter(lambda x : x%2 != 0,l))
print(a)

#12 the list after removing delete numbers which are divisible by 5 and 7 in [1,2,24,12,35,88,70,97,155]
l=[1,2,24,12,35,88,70,97,155]
a=list(filter(lambda x : x%5 == 0 and x%7 == 0,l))
print(a)

#13 list after removing the 0 th , 2 nd , 4 th ,6 th numbers in [12,24,35,70,88,120,153]
l=[12,24,35,70,88,120,153]
remove = [0,2,4,6]
a=[i for j,i in enumerate(l) if j not in remove]
print(a)


#14 program generate a 3*5*8 3D array whose each element is 0.

import pprint
a=[[[0 for i in range(3) ] for j in range(5)] for k in range(8)]
pprint.pprint(a)


#15 print the list after removing the 0 th , 4 th ,5 th , numbers in [12,24,35,70,88,120,155]
l=[12,24,35,70,88,120,155]
remove = [0,4,5]
a=[i for j,i in enumerate(l) if j not in remove]
print(a)


#16 print the list after removing the value 24 in [12,24,35,24,88,120,155]
l=[12,24,35,24,88,120,155]
a=[i for i in l if i!=24]
print(a)
'''

#17 list after removing all duplicate values with original order reserved.
from collections import OrderedDict
l=[12,24,35,88,120,155,89,155,55]
a=list(OrderedDict.fromkeys(l))
print(a)