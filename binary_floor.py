def bs(l,si,li,se):
    ceil=0
    mid=(si+li)//2
    if si<=li:
        if l[mid]==se:
            return l[mid]
        if l[mid]<se:
            return bs(l,mid+1,li,se)
        else:
            ceil=l[mid]
            return bs(l,si,mid-1,se)
    return l[mid]
l=list(map(int,input().split()))
se=int(input())
res=bs(l,0,len(l)-1,se)
print(res)