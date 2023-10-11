def check(arr):
    for i in range(len(arr)):
        for j in range(1,len(arr)):
            if arr[i]+arr[j]==target_sum:
                return [i,j]
arr=list(map(int,input().split()))
target_sum=int(input())
res=check(arr)
print(res)