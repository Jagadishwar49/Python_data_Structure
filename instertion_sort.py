def insertionSort(l):
    for s in range(0,len(l)):
        j=s
        while (j>0 and l[j]<l[j-1]):
            (l[j],l[j-1])=(l[j-1],l[j])
            j=j-1
    print(l)
insertionSort([9,3,1,5,7,2,8])
