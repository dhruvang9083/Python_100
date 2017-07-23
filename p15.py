s=str(input())
upper=0;
lower=0;
for i in range(0,len(s)):
	if s[i].isupper():
		upper=upper+1;
	elif s[i].islower():
		lower=lower+1;
print("upper case is",upper)
print("lower case is ",lower)