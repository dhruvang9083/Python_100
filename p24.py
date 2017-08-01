#the numbers divisible by 3 but not a multiple of 5 between the range of two numbers

x= int(input("starting number :"))
y= int(input("ending number :"))
l=[]
for i in range(x,y+1):
	if (i%3==0 and i%5!=0):
		l.append(i)
print (l)