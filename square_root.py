def exact_sqrt(number,epsilon=1e-6):
    if number<0:
        raise ValueError("Cannot compute the square root")
    if number<1:
        left,right=number,1
    else:
        left,right=0,number
    while abs(left-right)>epsilon:
        mid=(left+right)/2
        mid_sq=mid*mid
        if mid_sq<number:
            left=mid
        else:
            right=mid
    return (left+right)/2
def sqrt_(x,si,li,floor):
    if x==0 :
        return 0
    if x==1 or x==2:
        return 1
    if si<=li:
        mid=(si+li)//2
        sq=mid*mid
        if sq==x:
            return mid
        elif sq<n:
            floor=mid
            return sqrt_(x,mid+1,li,floor)
        else:
            return sqrt_(x,si,mid-1,floor)
    return floor
n=int(input())
print(f"The floor square root of {n} is {sqrt_(n,0,n,-1)}")
print(f"The exact square root of {n} is {exact_sqrt(n)}")