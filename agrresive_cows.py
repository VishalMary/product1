def can_i_place_my_cows(arr,min_dist,cows):
    last=arr[0]
    count=1
    for i in range(1,len(arr)):
        if abs(last-arr[i])>=min_dist:
            count+=1
            last=arr[i]
    if count>=cows:
        return True
    else:
        return False
def solve(arr,cows):
    limit=max(arr)-min(arr)
    for i in range(1,limit+1):
        if can_i_place_my_cows(arr,i,cows)==True:
            continue
        else:
            return i-1
arr=[0,3,4,7,9,10]
cows=3
res=solve(arr,cows)
print(res)
        