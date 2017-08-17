l=[]
l1=[]
a = 'abcdefghijklmnopqrstuvwxyz'
print (len(a))
#p=a.split(',')
#l.append(p)
#print(l)
b = str(input())
print(len(b))
#c=b.lower()
#d=c.split(' ')
#print(d)
for i in range(0,26):
	p=a[i].split(' ')
	l.append(p)
	for j in range(0,len(b)):
		q=b[j].split(' ')
		l1.append(q)
print(l)
print(l1)