a = 83
t = type(a)
print(t)  # <class 'int'>
i = float(a)
print(type(i))  # 83.0
b = 3.14
t = type(b)
print(t)  # <class 'float'>
c = 1 + 2j
t = type(c)
print(t)  # <class 'complex'>
d = "Hello"
t = type(d)
print(t)  # <class 'str'>
e = [1, 2, 3]
t = type(e)
print(t)  # <class 'list'>
f = (1, 2, 3)
t = type(f)
print(t)  # <class 'tuple'>
g = {1, 2, 3}
t = type(g)
print(t)  # <class 'set'>
h = {'name': 'Alice', 'age': 30}
t = type(h)
print(t)  # <class 'dict'>
i = True
t = type(i)
print(t)  # <class 'bool'>
j = None
t = type(j)
print(t)  # <class 'NoneType'>  