a=input()
s=len(a)
a=int(a)
l=[]
for i in range(s):
  c=a%10
  a=a//10
  if c%2!=0:
    l.append(str(c))
l.reverse()
print(' '.join(l))
