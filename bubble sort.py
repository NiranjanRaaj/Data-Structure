l=list(input().split())
le=len(l)
for j in range (le):
	for i in range (le-1):
		if l[i]>l[i+1]:
			l[i],l[i+1]=l[i+1],l[i]
	print(l)