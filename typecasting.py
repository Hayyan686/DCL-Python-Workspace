#bool -> int -> float -> complex
word = "India won against pakistan in U19 Asiacup"
print(len(word.split(" ")))
b = True
i = 2.1
c = 0j
print(b+c) #here bool data type is type casted into complex
print(type(i+c))

#explicit type casting
print(int(i))
#print(float(c)) # typeError: float can have only real value