print("1.---capitalize---")
s = "  dhee coding labs   "
s1 = "767486-24443"
print(s.capitalize())

print("\n2.---title---")
print(s.title())

print("\n3.---upper---")
print(s.upper())

print("\n4.---lower---")
print(s.lower())

print("\n5.---isupper---")
print(s.isupper())

print("\n6.---islower---")
print(s.islower())

print("\n7.---swapcase---")
print(s.swapcase())

print("\n8.---count---")
print(s.count('d'))

print("\n9.---index---")
print(s.index('d'))
print(s.index('d',3,12)) #--> here 3 is start index and 12 is end index

print("\n10.---startswith---")
print(s.startswith('dh'))

print("\n11.---endswith---")
print(s.endswith('s'))

print("\n12.---isalpha---")
print(s.isalpha())

print("\n13.---isdigit---")
print(s1.isdigit())

print("\n14.---isalnum---")
print(s1.isalnum())

print("\n15.---lstrip---")
print(s.lstrip())

print("\n16.---rstrip---")
print(s.rstrip())

print("\n17.---strip---")
print(s.strip())

print("\n18.---replace---")
print(s.replace('d',''))

print("\n19.---split---")
print(s.split(" "))
print(s1.split('-'))

print("\n20.---join---")
words = ['Tom', 'Jarry', 'Ben10']
print(' and '.join(words))
dates = ['15','08','1947']
print('/'.join(dates))
