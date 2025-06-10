def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while i+j<m+n:
        if(i==m):
            c.append(b[j])
            j=j+1
        elif(j==n):
            c.append(a[i])
            i=i+1
        elif(a[i]<=b[j]):
            c.append(a[i])
            i=i+1
        elif(a[i]>b[j]):
            c.append(b[j])
            j=j+1
    return(c)

def mergeSort(A,l,r):
    if(r-l<=1):
        return(A[l:r])
    if r-l>1:
        mid=(r+l)//2
        L=mergeSort(A,l,mid)
        R=mergeSort(A,mid,r)
        return(merge(L,R))
print(mergeSort([7,1,4,7,8,321,6],0,7))







