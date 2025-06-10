def factors(n):
    x=[]
    for i in range(1,n+1):
        if(n%i==0):
            x=x+[i]
    return(x)

def isPrime(x):
    if(factors(x)==[1,x]):
        return True
    else:
        return False

def nPrime(n):
    i=1
    c=[]
    while(i<n):
        if(isPrime(i)):
            c=c+[i]
        i=i+1
    return(c)

print(nPrime(50))
