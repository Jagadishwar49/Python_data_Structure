""" recusion is inductive of any function """

def lenghtOfList(l):
    
    if(l==[]):
        return 0
    else:
        return(1+lenghtOfList(l[1:]))

print(lenghtOfList([1,23,45,6,7,8]))

def sumOfList(l):
    
    if(l==[]):
        return 0
    else:
        return(l[0] + sumOfList(l[1:]))

print(sumOfList([1,23,45,6,7,8]))

""" maxiumn recurion aloowed is 997"""
"""we can use sys import to set max recuresion"""
