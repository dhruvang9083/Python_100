#bank details deposite and withdraw
import sys
total=0;
entry=int(input())
for i in range(0,entry):
	print("what you want W or D :")
	val=str(input())
	if val=='D':
		print("how much amount: ")
		amount = int(input())
		total=total+amount;
	elif val=='W':
		print("how much amount: ")
		amount = int(input())
		total=total-amount;
print("Final Balance is :",total)
