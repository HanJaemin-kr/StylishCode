# 바닥 타일 공사
""" n x 2 타일바닥을 ( 1x2, 2x1, 2x2 )를 이용해서 매꾸는 총 경우의 수"""

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[n])
print(d[0:10])