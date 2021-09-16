# 1로 만들기
"""주어진 입력 변수에 대해서 5 or 3 or 2로 나누거나 1을 빼서 1을 만들려고 한다.
이때 가질 수 있는 가장 최소한의 단계를 구하라
점화식 = a = min(a_i/3 , a_i/2 , a_i/5 , a_i/1 """

dp = [0] * 30001
x = int(input())

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[ i // 2 ]+1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3 ] + 1)

    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[0:10])
print(dp[x])