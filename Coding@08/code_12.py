n , k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort(reverse=True)
res = 0

for i in range(n):
    if(i < k):
        a[-(i+1)] , b[i] = b[i] , a[-(i+1)]
    res += a[i]
    print(a[i])

print(res)


# sol
"""
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
    
print(sum(a))
"""
