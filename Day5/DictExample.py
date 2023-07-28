d1 = {101:'abc',102:'bcd',103:'cde'}
print(type(d1))
print(d1[101])
print(d1)
d1[104]='efg'
d1[102]='xyz'
print(d1)
d1.pop(103)
print(d1)