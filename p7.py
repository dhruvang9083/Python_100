import math
c=50
h=30
l=[]
for i in range (0,3):
	d=int(input("Enter the value of d:" ))
	p=(2*c*d)/h
	q=math.sqrt(p)
	print (q)
	l.append(q)
print (l)