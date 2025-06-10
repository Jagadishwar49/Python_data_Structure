def selectionSort(l):
    for i in range(0,len(l)):
        for j in range(i,len(l)):
            if(l[i]>l[j]):
                (l[i],l[j])=(l[j],l[i])
    print(l)
selectionSort([2,6,1,3,5,9,7])
