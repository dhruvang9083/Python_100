#all the numbers into the dictionary with the (j, j**j)
x=int(input("enter the number : "))
dict={}
for i in range(1,x+1):
	dict[i]=i**i
print(i,dict)
