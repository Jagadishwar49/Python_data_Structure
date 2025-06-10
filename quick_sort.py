def quickSort(A,l,r):
    if r-l<=1:
        return()
    yellow = l+1
    for green in range(l+1,r):
        if(A[green]<=A[l]):
            (A[yellow],A[green])=(A[green],A[yellow])
            yellow=yellow+1
    (A[l],A[yellow-1])=(A[yellow-1],A[l])
    quickSort(A,l,yellow-1)
    quickSort(A,yellow,r)
l=[2,34,5,65,6,34,6]
print(quickSort(l,0,len(l)))
print(l)
