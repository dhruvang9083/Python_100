l=[]
x= int(input("enter the number of values"))
for i in range(0,x):
    values=str(input())
    l.append(values)
print (l)    
t=tuple(l)
print (t)
