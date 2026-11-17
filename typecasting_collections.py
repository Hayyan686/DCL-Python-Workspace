#implicit type casting is not applicable for collections
l = [10,20,30]
t = (11,22,33)
s =  {7,8,9}
st = "python"
d = {4:40, 5:50, 6:60}

print("list -> *")
print(tuple(l))
print(set(l))
print(str(l))
#print(dict(l)) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

print("\ntuple -> *")
print(list(t))
print(set(t))
print(str(t))
#print(dict(t)) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

print("\nstring ->*")
print(list(st))
print(tuple(st))
print(set(st))
#print(dict(s)) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

print("\nset -> *")
print(list(s))
print(tuple(s))
print(str(s))
#print(dict(s)) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

print("\n dictionary -> *")
# by default only keys are typecasted and returned
# to add values or entire items, use values() and items() methods of dictionary
print(list(d))
print(tuple(d))
print(str(d))
print(set(d))

# collection <- single value
i = 8+3j
print(str(i))

# collection -> single value
#str 
st = "10.1"
#print(int(st)) # error as it is in float dt
print(float(st))
print(bool(st))
print(complex(st))

