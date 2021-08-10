#떡볶이 집 떡만들기
"""적어도 m만큼의 떡을 가져가기 위한 최대값 h(떡 자르는 길이)를 구하여"""

n, m = input().split()
rice_cakes = list(map(int, input().split()))
start = 0
end = max(rice_cakes)

res = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in rice_cakes:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1

    else:
        res = mid
        start = mid + 1

print(res)