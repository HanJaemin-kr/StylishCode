col, row = map(int, input().split())

ice_class = []
for _ in range(col):
    ice_class.append(list(map(int, input())))
check =[[0] * row for i in range(col)]

def dfs(x,y):
    if x <= -1 or x >= col or y <= -1 or y >= row:
        return False
    if ice_class[x][y] == 0:
        ice_class[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1, y)
        return True

    return False

res = 0
for i in range(row):
    for j in range(col):
        if dfs(i,j) == True:
            res +=1

print(res)
