from  random import randint
def qs(lis):
	if len(lis)<=1:
		return lis
	p=l[randint(0,len(lis)-1)]
	small,equal,greater=[],[],[]
	for i in lis:
		if i<p:
			small.append(i)
		elif i==p:
			equal.append(i)
		elif i>p:
			greater.append(i)
			
	return qs(small)+equal+qs(greater)
	
	
l=list(input().split())
s=qs(l)
print(*s)

