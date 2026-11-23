print("-----Arithematic Operators-----")
print(f"Addition: {5+2}")
print(f"Subtaction: {5-2}")
print(5*2)
print(5/2)
print(5//2)
print(5%2)
print(5**2)

print("\n-----Assignment Operators-----")
a = 12
a += 7
print(a)

a = 12
a -= 7
print(a)

a = 12
a *= 7
print(a)

a = 12
a /= 7
print(f"{a:.2f}")

a = 12
a //= 7
print(a)

a = 12
a %= 7
print(a)

a = 12
a **= 7
print(a)

print("\n-----Relational Operators-----")
print(5==2)
print(5!=2)
print(5>2)
print(5<2)
print(5>=2)
print(5<=2)

print("\n-----Logical Operators-----")
print("AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("\nOR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print("\nNOT")
print(not True)
print(not False)

print()
print(1 and 4)
print(8 or 4)

print("\n-----Membership Operators-----")
#in #not in
l = [10,20,30,40,50]
print(60 in l) #False

t = (11,22,33)
print(22 not in t) #False

s = "Yadgiri"
print(' ' in s)

d = {21:'kartik'}
print('kartik' in d.values())


print("\n-----Identity Operators-----")
#is  #is not
a = 5
b = a
c = 5
print(a is b)
print(a is c)

l1 = [10,20,30]
l2 = [10,20,30]
print(l1 is l2)

print("\n-----Bitwise Operators-----")
print(1 & 0) #and
print(1 | 0) #or
print(1 ^ 2) #xor
print(~3)    #not
a = 200
print(a<<2)
print(pow(2,6))
b=131
print(b>>2)
print(b//pow(2,2))
