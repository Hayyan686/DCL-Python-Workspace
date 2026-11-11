print("-------------Dictionary Methods-------------")
#setdefault
print("1.---setdefault---")
d1 = {10:100,20:400,30:900}
d1.setdefault(40,1600)
d1.setdefault(50) #default as None
print(d1)

#update
print("\n2.---update---")
d2 = {1:11,2:22,3:33}
d1.update(d2) #copies and add d2 items in d1
print(d1)

print("\n3.---get---")
print(d1.get(1)) 
print(d1.get(12)) #None is returned

print("\n4.---pop---")
poped = d1.pop(2) #item is removed and returns only value
print(poped)
print(d1)

print("\n5.---popitem---")
popitem = d1.popitem() #remove and returns last item from the dict in the form of tuple
print(popitem)

print("\n6.---clear---")

d2.clear() #it removes all the items from the dict
print(d2)

print("\n7.---keys---")
print(d1.keys()) #it returns all key in the form of list

print("\n8.---values---")
print(d1.values()) #it returns all values in the form of list

print("\n9.---items---")
print(d1.items()) #it returns list of all key-value pairs, each pair is in the form of tuple
