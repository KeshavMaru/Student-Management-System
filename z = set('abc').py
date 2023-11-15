a = '12','45','6','74'
b = 'ram','sham','uv','ig'
l1 = a.split(",")
l2 = b.split(",")
s1 = set(l1)
print(s1)
print(sorted(s1))
d1 = dict(zip(l1,l2))
print(d1)
print(sorted(d1.items()))