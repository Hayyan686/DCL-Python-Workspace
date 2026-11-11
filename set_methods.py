print("---add---")
s1 = {10,20,30}
s1.add(20)
print(s1)

print("---update---")
s2 = {30,40,50}
s1.update(s2)
print(s1)

print("---pop---")
s1.pop()
print(s1)

print("---remove---")
#s1.remove(11) #keyError
s1.remove(10)
print(s1)

print("---discard---")
s1.discard(22)
s1.discard(30)
print(s1)

print("---clear---")
s1.clear()
print(s1)

print("---issubset---")
s3 = {1,4,6,2,7}
s4 = {3,4,2,5,6,1}
res = s3.issubset(s4)
print(res)

print("---issuperset---")
r = s4.issuperset(s3)
print(r)

print("---isdisjoint---")
r =s3.isdisjoint(s4)
print(r)

print("---union---")
s5 = s3.union(s4)
print(s5)

print("---intersection---")
s6 = s3.intersection(s4)
print(s6)
sett = {34,35}
s7 = s3.intersection(sett)
print(s7)

print("---difference---")
s8 = s3.difference(s4)
print(s8)

print("------")
s9 = s3.symmetric_difference(s4)
print(s9)
