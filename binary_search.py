print ('Hello World')
def binarySearch(l,a,b,v):
    mid = int((a+b)//2)
    if(mid<0):
        return(False)
    if v==l[mid]:
        return(True)
    elif v < l[mid]:
        return binarySearch(l,a,mid,v)
    else:
        return binarySearch(l,mid,b,v)

a=[1,2,3,4,5]
print(binarySearch(a,0,len(a),1))
