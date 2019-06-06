a,b,c=input("enter the number").split()
if((a>b) and (a>c)):
    print(a)
elif((b>c) and (b>a)):
    print(b)
else:
    print(c)
