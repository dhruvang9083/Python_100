x=int(input('enter the number'))
factorial=1
if x==0:
    print (1);
else:
    for i in range(1,x+1):
        factorial= i*factorial
    print (factorial)
