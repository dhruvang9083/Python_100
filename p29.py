l=[]
for i in range(0,100):
	l.append(i)
print("number list 1 to 100","\n\n",l)
print("\n")
result=list(filter(lambda x : x%2==0,l))
print("divisible by 2 list is","\n\n",result)
