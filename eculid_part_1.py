def gcd(m,n):
    if(m<n):
        (m,n)=(n,m)
    if(m%n==0):
        return(n)
    else:
        diff = m-n
        return(gcd(max(n,diff),min(n,diff)))
print(gcd(12,66))
print(gcd(101,2))
print(gcd(5,3))
print(gcd(22,7))
print(gcd(8,4))
