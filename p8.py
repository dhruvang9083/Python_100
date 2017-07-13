row=int(input())
column=int(input())
l=[[0 for i in range (column)] for j in range (row)]
for i in range(row):
	for  j in range(column):
		l[i][j]=i*j
print(l)