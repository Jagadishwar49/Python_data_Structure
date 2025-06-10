def binarySearch(l,a,b,v):
    mid = int((a+b)//2)
    if(mid<=0):
        return(False)
    if v==l[mid]:
        return(True)
    elif v > l[mid]:
        return binarySearch(l,mid+1,b,v)
    else:
        return binarySearch(l,a,mid,v)

print(binarySearch([1,2,3,4,5],0,6,1))
