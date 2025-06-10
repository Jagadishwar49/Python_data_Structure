# This Most efficent euclid algorithm because earlier method we were finding diffrence but think id we want to find 
# GCD of 101 and 2 the it start for 101-2=99 ..97..95...ect it would take 50 step 

def gcd(m,n):
    if(m<n):
        (m,n)=(n,m)

    while m%n !=0:
        (m,n)=(n,m%n)
    return(n)

print(gcd(101,2))
print(gcd(66,6))
