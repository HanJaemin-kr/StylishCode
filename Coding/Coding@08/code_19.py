# 효율적인 화폐규성
"""
n 종류의 화폐에서 개수를 최소한으로 하여 합이 M이 되도록 만든다 할 때
각 화폐는 몇개라도 사용가능하고, 구성은 같되 순서만 다른것은 같은 경우라고 구분한다.

"""

n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[ j - array[i] ] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])