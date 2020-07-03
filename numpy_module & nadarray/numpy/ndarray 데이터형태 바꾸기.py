import numpy as np

#ravel,np.ravel 다차원배열을 1차원으로 변경
# c와 f가 있는데 c는 행우선변경 f는 열우선 변경

x = np.arange(15).reshape(3,5)
print(x)
print(np.ravel(x,order='F'))
x.ravel()
print(x)

#flatten()
y = np.arange(15).reshape(3,5)
t2 = y.flatten()
print(t2)
print(y)

#reshape()

z = np.arange(36).reshape(-1,6)
print(z)