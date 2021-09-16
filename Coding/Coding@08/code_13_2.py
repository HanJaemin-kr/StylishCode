#부춤 찾기를 계수 정렬을 이용하여 풀이하기

n = int(input())
data = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

product_list = [0] * 11

for list_index in data:
    product_list[list_index] += 1

for i in finds:
    if ( product_list[i] > 0):
        print("yes", end=' ')
    else:
        print('no', end=' ')


""" 교제 솔루션
n = int(input())
array = [0] * 100001

for i in input().split():
    array[int(i)] = 1
    
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes')
    else:
        print('no')
"""