import math
mi=int(input())
l=math.log10(mi)/math.log10(2)
if math.ceil(l)==math.floor(l):
	print(0)
else:
	a=(mi-1)//2
	b=a*2
	print(mi-b)
