a=int(input())
s=0
while(a>0):
    x=a%10
    a=a//10
    s=(s*10)+x
print(s)   
