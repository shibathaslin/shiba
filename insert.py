#shiba
m,n=input().split()
q=0
if len(a)>len(b):
  m,n=n,m
i=0
while i<len(m):
  q+=(ord(n[i])-ord(m[i]))
  i+=1
for i in range(i,len(n)):
  q+=ord(n[i])-ord('m')+1
print(q)
