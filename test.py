import numpy as np

x = np.array([1, 2])
print(x)

w = np.array([[4, 8], [6, 3]])
print(w)

t = x.dot(w)
print(t)

y = np.array([1, 4, 7])
z = np.array([[2, 8, 7], [1, 9, 3], [6, 4, 0]])

o = y.dot(z)
print(o)

x = np.array([[4, 5], [3, 6]])
print(x)
y = np.array([[7], [4]])
print(y)

r = x.dot(y)
print(r)
