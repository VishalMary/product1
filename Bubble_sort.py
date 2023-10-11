l=list(map(int,input().split()))
n=len(l)
flag=False
for i in range(1,n):
    for j in range(n-i):
        if l[j]>l[j+1]:
            flag=True
            l[j],l[j+1]=l[j+1],l[j]
while flag==False:
    break
flag=False
for i in l:
    print(i,end=" ")