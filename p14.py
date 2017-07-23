# calculate number of letters nd digits in setences
s=str(input())
digit=0
letters=0
l=[]
for i in range(0,len(s)):
	# digit=""
	if s[i].isdigit():
		digit=digit+1
		#print(digit)
	elif s[i].isalpha():
		letters=letters+1 
print("letter is",letters)
print("digit is",digit)
l.append(letters)
l.append(digit)
print(l)