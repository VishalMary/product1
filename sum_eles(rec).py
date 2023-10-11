def find_sum(arr):
    if len(arr)==0:
        return
    if len(arr)==1:
        return arr[0]
    mid=len(arr)//2
    li=find_sum(arr[:mid])
    ri=find_sum(arr[mid:])
    return li+ri
arr=list(map(int,input().split()))
print(find_sum(arr))