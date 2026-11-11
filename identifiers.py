import keyword
print(keyword.kwlist)
count = 0
print(len(keyword.kwlist))
for i in keyword.kwlist:
    count +=1
print(count)

