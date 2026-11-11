empty_list = list()  #1st way
empty_list1 = []   #2nd way
print(empty_list)
print(type(empty_list))
print(list())
print(len(list()))

marks = [67,89,45,43,90]
print(len(marks))
print(marks[4]) #printing specific indexed marks

marks[3] = 45 #modifying list
print(marks)


marks[8] = 45 #Index out of range error

