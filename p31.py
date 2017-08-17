#1 int into string
'''
def conv():
	a = str(input())
	b = a.split(' ')
	print (b)
conv()

#4 string concate

s1=str(input())
s2=str(input())
def add(a,b):
    return a+" "+b
print (add(s1,s2))

#3 two integral number nad add it

def add(s1,s2):
	s1 = str(input())
	s2 = str(input())
	s3 = s1+s2
	print(s3)
add(1,2)


#5 max length print and if same then print both string

def length1():
	s1 = str(input())
	s2 = str(input())
	if(len(s1)>len(s2)):
		print(s1)
	elif(len(s1)==len(s2)):
		print(s1,s2)
	else:
		print(s2)
length1()
'''

#6 even odd number ptint

def number(a):
	a=int(input())
	if(a%2==0):
		print(a,"number is even")
	else:
		print(a,"number is odd")
number(122)

#7 dict 1 to 3 square
'''
dict={}
def square():
	for i in range(0,4):
		dict[i]=i*i
	print(dict)
square()

#8  1 to 21 square dict

dict = {}
def square():
	for i in range(1,21):
		dict[i] = i*i
	print(dict)
	print(dict.keys())
	print(dict.values())
square()

#10 list of square 1 to 21

l=[]
def square():
	for i in range(1,21):
		a=i*i
		l.append(a)
	print(l)
square()

#11 prog 10 and print 5 elements first

l=[]
def square():
	for i in range(1,21):
		a=i*i
		l.append(a)
	print(l[0:5])
square()

#12 prog 10 and tupple list

l=[]
t=()
def square():
	for i in range(1,21):
		a=i*i
		l.append(a)
		t=tuple(l)
	print(t)
square()

#13 splice tuple list

t = (1,2,3,4,5,6,7,8,9,10)
def half():
	print(t[0:5])
	print(t[5:])
half()

#14 even number tuple

t=(1,2,3,4,5,6,7,8,9,10)
l=[]
def even():
	for i in range(0,len(t)):
		if(t[i]%2==0):
			l.append(t[i])
	print(l)
even()

#15 find even number using filter

l=[1,2,3,4,5,6,7,8,9,10]
a=list(filter(lambda x : x%2==0,l))
print(a)

#16 square of elements using map

l=[1,2,3,4,5,6,7,8,9,10]
a=list(map(lambda x : x*x,l))
print(a)

#17 filter and map square of even number 

l=[1,2,3,4,5,6,7,8,9,10]
a=list(map(lambda x:x**2,filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10])))
print(a)

#18 even number between 1 to 20

a=list(filter(lambda x : x%2==0,range(1,21)))
print(a)

#19 square of number between 1 to 20 using map

a=list(map(lambda x : x*x,range(1,21)))
print(a)
'''