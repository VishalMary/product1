'''Sort colors 0,1,2 using count sort'''
nums=list(map(int,input().split()))
count=[0]*len(nums)
for i in range(len(nums)):
    count[nums[i]]+=1
for i in range(1,len(count)):
    count[i]+=count[i-1]
res=[0]*len(nums)
for i in range(len(nums)):
    res[count[nums[i]]-1]=nums[i]
    count[nums[i]]-=1
for i in res:
    print(i,end=" ")
