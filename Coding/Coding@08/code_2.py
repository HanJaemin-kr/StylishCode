# 큰 수의 법칙 
""" 배열 크기 N , 숫자 더한 횟수 M, 최대 연속 가능한 인덱스 횟수 K
첫 째줄에 N (2 < N < 1000) , M (1 < m < 10000) , K (1 < K < 10000)의 자연수가 주어지고 , 각 자연수는 공백 구분
두번 째 줄에 N개의 자연수가 주어지며 각 자연수는 1이상 10000이하
입력으로 주어지는 K는 항상 M보다 작거나 크다 

주어진 수들을 M번 더하여 가장 큰 수를 만들어라 단, 배열의 특정한 인덱스에 해당하는 수가 연속으로 K번을 초과하여 더해질 수 없다. 
예 2,4,5,4,6 > (M:8 K:3) > 6+6+6+5+6+6+6+5 = 46 
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort() 
Big_data_1 = data[n-1]
Big_data_2 = data[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result += count * Big_data_1
result += (m-count) * Big_data_2 

print(result)



