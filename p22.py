x=int(input("enter the number"))
l=[]
a=[]
b=[]
h=[]

for i in range(1,x+1):
	l.append(i)
print("number list is",l)
for i in range(1,x+1):
	if(i%2==0):
		a.append(i)
print("Even number list is",a)

for i in range(1,x+1):
	if(i%2==1):
		b.append(i)
print("odd number list is",b)

for i in range(1,x+1):
	if i>1:
		for j in range(2,i):
			if (i%j)==0:
				break;
		else:
			print(i)