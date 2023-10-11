def mergesort(l,inversion):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        li=mergesort(left,inversion)
        ri=mergesort(right,inversion)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                l[k]=left[i]
                i=i+1
                k=k+1
            else:
                l[k]=right[j]
                j=j+1
                k=k+1
                inversion+=len(left)-i
        while i<len(left):
            l[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            l[k]=right[j]
            j=j+1
            k=k+1
        return li+ri+inversion
    return 0
l=[2,3,5,6,1,4,7]
print(mergesort(l,0))
print(l)

                
            
                
        