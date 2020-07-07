import numpy as np

x = np.arange(15).reshape(3,5)
print(x)

print(np.sum(x, axis=0))
print(np.sum(x, axis=1))
print(np.sum(x,axis=(0,1)))

y = np.arange(36).reshape(3,4,3)
print(y)

print(np.sum(y,axis=1))

