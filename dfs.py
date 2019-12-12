t=int(input())
d=[]
for i in range(t):
    l=[]
    lis=[]
    n=int(input())
    l=list(input().split())
    r=-1
    mn=0
    for k in range(len(l)-mn):
        m=l.count(int(r))
        mn=m
        e=0
        for x in range(m):
            lis.append(int(e))
        e=e+1
        ind=0
        for g in l:
            if g == r:
                n=ind
                break
            ind=ind+1
    mc=0
    depth=0
    for y in lis:
        c=lis.count(int(y))
        if mc<=int(c):
            mc=c
            depth=y
    d.append(depth)
for z in range(len(d)):
    print(d[z])
