from itertools import combinations
m,n=map(int,input().split())
p=len(str(m))
Y=list(combinations(str(m),p-n))
y=(sorted(Y))
Q="".join(y[0])
print(Q)
