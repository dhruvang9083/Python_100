n =input("enter the string")
length = int(len(n))
for i in range(0,len(n)+1):
    for j in range(i+3,len(n)+1): #i+3 minimum 3 characters for pelindrom
        n1=n[i:j] #devided string to sub-string
        print(n1)
        n2 =n1[::-1] #reverse sub-string
        print(n2)
        if(n1==n2):
            print("pelindrom")
        else:
            print("not pelindrom")


