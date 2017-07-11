l=[]
a=0
b=1
while b<50:
    print (b);
    for i in range(0,b,a+b):
        l.append(b)
        print (l)
    a,b=b,a+b
