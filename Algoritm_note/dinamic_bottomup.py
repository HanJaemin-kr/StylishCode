d = [0] * 100   # dp테이블 초길하

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
	d[i] = d[i-1] + d[i-2]

