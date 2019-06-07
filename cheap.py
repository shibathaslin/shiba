m,n=input().split()
a=abs(len(m)-len(n))
for i in range(len(m)):
    if len(n)==1 and v[i] in m:
        break
    if m[i]!=n[i]:
        a=a+1
print(a)
