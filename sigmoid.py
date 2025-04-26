import numpy as np
import matplotlib.pyplot as plt

print(np.exp(1))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    
x = np.arange(-10, 10, 0.01)
y = sigmoid(x)

plt.clf()
plt.plot(x, y, "r")
plt.grid(True)
plt.show()