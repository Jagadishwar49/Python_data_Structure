s=(67,7,1999)
print(s[1])
"""s[1]=8 tuples is immuatble once declared it cannot we edited"""
""" tuples are same as list but immutable """
j=() #empty tuples declaratrion

"""

dict["test1"]["Dhawan"]=84 will result in error because dict["test1"] is not declared 

"""
dict={}
dict["test1"]={}
dict["test2"]={}
dict["test1"]["Dhawan"]=84
dict["test2"]["Dhawan"]=35
dict["test2"]["kolhi"]=55
dict["test1"]["Kolhi"]=90
print(dict)
print(str(dict.keys))
print(str(dict.values))

totalMatch=0
for i in dict.values():
    totalMatch=len(i) 
print(totalMatch)

