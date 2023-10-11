def find_peak(arr):
    si=0
    li=len(arr)-1
    while (si<=li):
        mid=(si+li)//2
        if arr[mid+1]<arr[mid] and arr[mid-1]<arr[mid]:
            return mid
        elif arr[mid+1]>arr[mid]:
            li=mid+1
        else:
            si=mid
arr=list(map(int,input().split()))
print(find_peak(arr))