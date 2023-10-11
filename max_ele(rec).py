def find_max(arr,si,li):
    if si==li:
        return arr[si]
    mid=(si+li)//2
    left=find_max(arr,si,mid)
    right=find_max(arr,mid+1,li)
    return max(left,right)
arr=list(map(int,input().split()))
res=find_max(arr,0,len(arr)-1)
print(res)
    