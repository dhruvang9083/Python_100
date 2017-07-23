s=int(input("enter the list number "))
l=[]
for i in range(0,s):
	v=int(input())
	if(v%2!=0):
		l.append(v)
print(l)