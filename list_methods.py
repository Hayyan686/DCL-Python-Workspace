
print("---append---")
list1 = []
list1.append(4)
print(list1)
list1.append(5)

print("-------------------------")
print("---insert---")
list2 = [20,40,60,80]
list2.insert(-21,100)
print(list2)
list2.insert(-2,6)
print(list2)

print("-------------------------")
print("---extend---")
l3 = [11,22,33]
l4 = [44,55,66]
print(l3+l4) #extending using concatination
l3.extend(l4)
print(l3)

print("-------------------------")
print("---pop---")
l4 = [10,20,30,40]
ele = l4.pop()
print(l4)
print(f"{ele} is removed")
ele2 = l4.pop(1)
print(f"{ele2} is removed")

print("-------------------------")
print("---remove---")
l6 = [30,40,20,50]
print(f"orginal list:\n{l6}")
removed = l6.remove(20) # remove will not return
print(f"{removed} is removed")
print(l6)

print("-------------------------")
print("---clear---")
l7 = [43,45,76,23,68]
print(l7)
l7.clear()
print(f"List is cleared {l7}")

print("-------------------------")
print("---sort---")
l7 = [43,45,76,23,68] # only sortable datatype can be sorted.
                      #str is not sortable
print(l7)
l7.sort()
print(f"sorted list: {l7}")

print("-------------------------")
print("---reverse---")
print(l7)
l7.reverse()
print(l7)

print("-------------------------")
print("---count---")
l9 = [56,23,1,54,76,54,23,67]
c = l9.count(54)
print(c)

print("-------------------------")
print("---index---")
ind = l9.index(23)
print(ind)
ind = l9.index(23,3) #=> custom start index(Inclusive)
print(ind)
ind = l9.index(23,3,7) #=> custom stop index(Exclusive)
print(ind)
