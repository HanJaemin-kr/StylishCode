# 1이 될때까지
""" 어떠한 수 N이 1이 될때 까지 1을 빼거나 k로 나누는 방법중 하나를 반복적으로 선택 수행한다.
두번째는 N이 k로 나누어 떨어질때만 선택 가능 이 때 두가지 방법중 효율적인 방법으로 최소횟수를 구하라 """
import math

n, k = map(int, input().split())
count = 0
while(n != 1):
    if(n % k != 0): # 숫자가 커진다면 게속 비교하는 횟수가 추가댐 
        n = n-1
    else:
        n = n/k
    count = count+1

print(count)
        



# so1 2

n, k = map(int, input().split())
res = 0


while True:
    target = (n // k) * k   # n에서 가장 근접한 k의 배수
    res += (n-target)   # 1을 빼서 근접한 배수로 가는 단계 수
    n = target
    if n<k:   #n이 k보다 작다면 뺄샘만 남음으로 반복문 종
        break
    n = n/k   # 나누기 처리 
    res += 1

res += (n - 1)

print(res)
