#anju
q,u=input().split()
q=int(q)
u=int(u)
at=[int(i) for i in input().split()]

w=[]
z=[]
for i in range(0,u):
    x,y=input().split()
    w.append(x)
    z.append(y)


for i in range(0,r):
    q=int(w[i])-1

    t=int(z[i])-1


    for j in range(1,au[q]+1):
        if (au[q]%j==0 and au[t]%j==0):
            gcd=j
    print(gcd)

