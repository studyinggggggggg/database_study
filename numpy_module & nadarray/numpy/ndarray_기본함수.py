import numpy as np

x = np.arange(15).reshape(3,5)
y = np.random.rand(15).reshape(3,5)
print(x)
print(y)

#연산 함수 (add, substract, multiply, divide)

print(np.add(x,y))
print(x + y)

#통계 함수 (평균, 분산, 중앙, 최대 ,최소값 등등 통계 관련된 함수가 내장)
#평균은 mean
print(np.mean(x))
print(y.mean())

#최대값은 max
print(np.max(x))

#가장 큰 값의 index 가져오기
print(np.argmax(x))

#집계함수 (합계, 누적합계)
print(np.sum(x, axis = 1))
print(np.sum(x, axis = 0))
print(np.cumsum(x))

#any, all 함수
#any : 특정 조건을 만족하는 것이 하나라도 있으면 True 아니면 False
#all : 모든 원소가 만족하는지 체크

z = np.random.rand(15)
print(z)
print(np.any(z < 0.5))
print(np.all(z < 0.5))

#where 함수
#조건에 따라 선별적으로 값을 선택 가능
z = np.random.rand(10)
print(z)
print(np.where(z > 0, -z , z))
