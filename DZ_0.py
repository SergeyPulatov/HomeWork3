a = "Sergey" #String
b = 24 #Integer
c = 24.5 #Float
d = b"d" #Bytes
e = ["e", "e", "e"] #List
f = (6, "Tuple", 6.6) #Tuple
g = set("Sergey") #Set
h = frozenset({0, 1, 2, 3, 4, 0, 1, 2, 3, 4}) #Frozen set
i = {"name": "Sergey", "age": "24"} #Dict

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(g, type(g))
print(h, type(h))
print(i, type(i))

x = "Sergey"
y = "Pulatov"
z = x + y
print(z)

print(x, b)

print(x + str(b))