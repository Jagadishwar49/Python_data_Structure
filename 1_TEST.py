
print ('\nselectionSort')
def selectionSort(l):
    for i in range(len(l)):
        for j in range(i,len(l)):
            if(l[i]>l[j]):
                (l[i],l[j])=(l[j],l[i])
    return(l)
    
print(selectionSort([8,4,7,3,1,6,8]))


print ('\ninsertionSort')

def insertionSort(l):
    for i in range(len(l)):
        pos=i
        while(pos>0 and l[pos]<l[pos-1]):
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            pos=pos-1
    return(l)
    
print(insertionSort([8,4,7,3,1,6,8]))

print ('\nmergeSort')

def merge(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while(i+j < m+n):
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
        mid =(r+l)//2
        L=mergeSort(A,l,mid)
        R=mergeSort(A,mid,r)
        return(merge(L,R))
        
print(mergeSort([8,4,7,3,1,6,8],0,7))

def quickSort(A,l,r):
    if(r-l<=0):
        return()
    yellow=l+1
    for green in range(l+1,r):
        if(A[green]<=A[l]):
            (A[green],A[yellow])=(A[yellow],A[green])
            yellow=yellow+1 
    (A[l],A[yellow-1])=(A[yellow-1],A[l])
    quickSort(A,l,yellow-1)
    quickSort(A,yellow,r)
l=[1,2,3,8,5,7,98,45,67,1]
quickSort(l,0,len(l))
print(l)

            

