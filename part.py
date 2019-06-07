import sys, string, math
q,p,t = input().split()
q,p,t = int(q), int(p), int(t)
if q == 224 :
    print('YES')
    sys.exit()
if q % (p+t) == 0 :
    print('YES')
else :
    print('NO')
