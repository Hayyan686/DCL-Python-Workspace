empty_dict = {} #1st apporach to create empty dict
print(type(empty_dict))
empty_dict2 = dict()#2nd apporach to create empty dict

d1 = {10:100, 20:400, 30:900}
print(d1)

# Access a value in dictionary
print(d1[10])

#modify
d1[20] = 500
print(d1[20])

#create
d1[21] = 700
print(d1)