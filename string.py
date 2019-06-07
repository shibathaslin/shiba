b=input()
b=int(b)
A=[]
for i in range(0,b):  
    y=input()
    A.append(y)
X=[]
for i in zip(*K):
    if i.count(i[0])==len(i): 
        X.append(i[0])
    else:
        break
print(''.join(X))
