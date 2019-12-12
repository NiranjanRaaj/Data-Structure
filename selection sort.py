l=list(input().split())
le=len(l)
m=-1
for i in range(le):
	m=i
	print('pass',m)
	for j in range(i,le):
		if l[j]<l[m]:
			m=j
			
	l[m],l[i]=l[i],l[m]

	print(l)
	
print(l)
			

			
			
	