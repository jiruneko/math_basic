import numpy as np

x = np.array([[1,2],
            [3,4]])

y = np.array([[5, 6],
            [7,8]])

print(x + y)


w = np.array([[3, 5],
              [4, 2]])
x = np.array([[7], [8]])

b = np.array([[1], [1]])

a = w.dot(x) + b

print(a)