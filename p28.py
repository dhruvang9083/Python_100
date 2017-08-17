'''#try to use Lambda, Filter, Map and Reduce function
s = str(input())
p = s.upper()
#z = p.split(' ')
print (p)
#for i in range(0,len(p)):
#	print("total character is",i)

x = int(input())
l=[]
for i in range(0,x):
	l.append(i)
print(l)
for i in range(0,x):
	dict[i]=i*i;
print(dict)
from functools import reduce
add=reduce(lambda num1,num2 : num1+num2,[1,2,3,4,5])
#sub=[15,10]
#sub=list(map(lambda num1,num2 : num1-num2,num1+num2))
#print(sub)
print(add)

f =list((lambda x : x*x)(x) for x in range(0,100,2))
#[f(x) for x in range(10)]
print(f)'''
'''l=[1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x : x % 2==0,l))
print(result)
'''
'''items=[1,2,3,4]
def sqr(x):
	return x*x
#result1=list(map(lambda x: x*x,l1))
result=list(map(sqr,items))
print(result)'''
def pan(s):
	p= not set('abcdefghijklmnopqrstuvwxyz')
	v = p-set(s.lower())
	print(v)
pan('hjvhvjkj')