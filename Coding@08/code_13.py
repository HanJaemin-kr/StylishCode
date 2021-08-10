# 부품 찾기
# 첫 리스트 크기 N의 리스트에서 M리스트의 요소가 있는지 없는지 확인

def find_product(data, find_x, start, end):
    mid = (start + end) // 2
    if (start > end):
        print('no', end=' ')
        return False

    if (data[mid] == find_x):
        print('yes', end=' ')
        return True

    elif (data[mid] > find_x):
        find_product(data, find_x, start, mid - 1)
    else:
        find_product(data, find_x, mid + 1, end)


n = int(input())
data = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

data.sort()
for i in range(m):
    find_product(data, finds[i], 0, n)


""" 집합 자료형 이용

n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end='')
    else
        print('no', end='')

"""