#write a program to sort the (name, age, height) tuples by ascending order
number = int(input("enter the total entry"))
t=()
l=[]
for i in range(0,number):
	name = str(input("enter the name"))
	age = int(input("enter Age"))
	height = int(input("enter height"))
	l.append(name)
	l.append(age)
	l.append(height)
print(l)
t=tuple(l)
print(t)
