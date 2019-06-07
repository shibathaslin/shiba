m1=int(input())
y=list(map(int,input().split()))
ci=0
for i in range(len(z)):
    for j in range(i+1,len(y)):
        for k in range(j+1,len(y)):
            if y[i]<y[j]<y[k] and i<j<k:
                ci += 1
print(ci)
