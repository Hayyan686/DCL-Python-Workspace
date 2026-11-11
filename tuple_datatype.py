t1 = (325)   
print(type(t1)) #int class
t1 = (325,) #tuple class 
print(type(t1))
print(len(t1))

t3 = (12,12,24,40)
print(t3[3])
print(len(t3))

print("---Tuple Methods---")
c = t3.count(12)
ind = t3.index(12)
print(f"count: {c}\nindex: {ind}")
