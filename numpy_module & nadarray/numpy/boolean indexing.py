import numpy as np

x = np.random.randint(1,100,size=100)
print(x)

even_mask = x % 2 == 0
print(even_mask)

print(x[x > 0])

temp = np.random.randint(1,20,size = 30)
print(temp)

print(len(temp[temp > 10]))
print(np.mean(temp[temp>10]))
