# List methods
a = ["apple", "mango", "orange", 3, 4, 5.0]
a.insert(6,'banana')
print(a)
print(a[-1:-6])
a[3] = "peach"
print(a)
a[3:5] = [1,2]
print(a)
a.insert(3, 'watermelon')
print(a)
a.append("apricot")
print(a)

b = ["tomato", "onion"]
a.extend(b)
print(a)

a.remove(1)
print(a)

a.remove('tomato')
print(a)

a.pop(2)
print(a)

a.pop()
print(a)

c= ['cucumber', 'potato']
del(c)
#print(c)

d= ['cucumber', 'potato', 'ginger']
d.clear()
print(d)


e= ['cucumber', 'potato', 'ginger']
e.sort()
print(e)

e.sort(reverse=True)
print(e)











