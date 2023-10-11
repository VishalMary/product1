arr=[0,1,0,2,1,0,1,3,2,1,2,1]
l=0
r=len(arr)-1
max_l=arr[0]
max_r=arr[r]
while l<r:
    res=0
    if max_l<max_r:
        l+=1
        if max_l<arr[l]:
            max_l=arr[l]
        res+=max_l-arr[l]
    else:
        r-=1
        if max_r<arr[r]:
            max_r=arr[r]
        res+=max_r-arr[r]
print(res)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''if left<right:
        for left in range(len(l)):
            mid=(left+right)//2
            left_arr=l[:mid]
            right_arr=l[mid:]
        max_l=0
        for i in range(len(left_arr)):
            if left_arr[i]>max_l:
                max_l=left_arr[i]
        print(max_l)
        max_r=0
        for i in range(len(right_arr)):
            if right_arr[i]>max_r:
                max_r=right_arr[i]
    return '''
