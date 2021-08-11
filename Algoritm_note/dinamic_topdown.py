d = [0] * 100

def fibo(x):

	if x == 1 or x ==2 :
		return 1

	if d[x] != 0:			# 이미 계산한 피보라면 계산 없이 반환
		return d[x]

	d[x] = fibo(x-1) + fibo(x-2)      #  계산하지 못한 문제에 대해서만 연산;
	return d[x]


