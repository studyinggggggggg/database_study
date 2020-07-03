import numpy as np

#1차원 행렬 인덱싱
x = np.arange(10)
print(x[0])

#2차원 행렬 인덱싱
x = np.arange(10).reshape(2,5)
print(x[0])
print(x[0,1])
print(x[0][1])

#3차원 행렬 인덱싱

x = np.arange(36).reshape(3,4,3)
print(x)


#1차원 백터 슬라이싱
x = np.arange(10)
print(x[1:7])

#2차원 벡터 슬라이싱
x = np.arange(10).reshape(2,5)
print(x[0,1:5])

#3차원 백터 슬라이싱
x = np.arange(60).reshape(2,10,3)
print(x)
print(x[1:2,3:4,0:1])