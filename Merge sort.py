l=list(input().split())
le=len(l)
#l1=l[:le//2]
#l2=l[le-1:(le//2)-1:-1]
l1=[]
l2=[]
for i in range(le//2):
  l1.append(l[i])
for j in range(le//2,le):
  l2.append(l[j])


l1.sort()
l2.sort()
print(l1)
print(l2)
full_list=l1+l2
full_list.sort()
print(full_list)
