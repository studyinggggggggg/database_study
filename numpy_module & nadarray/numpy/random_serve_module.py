import numpy as np

#0과 1사이의 값에서 2행 3열 출력
print(np.random.rand(2,3))

#정규 분포 생성하기
print(np.random.randn(3,4))

#특정 정수 사이에서 샘플링
print(np.random.randint(1,100, size = (3,5)))

#랜덤한 값을 동일하게 다시 생성하고자 할때 사용 seed를 호출하고 랜덤결과를 호출하면 동일한 값이 나옴. seed에 들어가는 숫자는 아무 숫자를 써도 된다. 고정값
print(np.random.seed(100))
print(np.random.randn(3,4))


#choice 1차원 ndarray로 부터 랜덤 숫자 샘플링
print(np.random.choice(100,size=(3,4)))
x = np.array([1,2,3,4,5,6])
print(np.random.choice(x,size=(2,2)))

#확률 분포에 따른 ndarray 생성
