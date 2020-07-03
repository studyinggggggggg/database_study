import numpy as np

x = np.array([1,2,3,4])

print(x)

y = np.array([[2,3,4],[1,2,5]])


a = np.arange(1,10,2)

print(a)

print(np.ones((2,4,5)))
print(np.zeros((2,4,5)))

print(np.empty((3,4)))

print(np.full((3,4),7))

print(np.eye(3))

print(np.linspace(1,10,5))

c = np.arange(1,16)
print(c.shape)
print(c.reshape(3,5))