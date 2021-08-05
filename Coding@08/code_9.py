# dfs로 계산한 미로찾기 문제
# 0을 피하여 끝에서 끝까지 갈 수 있는 최단거리


n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))
check = [ [0] * m for i in range(n) ]
res = n*m
print(maze)
print(check)
def dfs(x,y,move_count):
    global res

    if (x == n-1 and y == m-1):
        print("목적지 도 ")
        if (res > move_count):
            res = move_count
        return True

    if (x>n-1 or x<=-1 or y>m-1 or y<=-1):
        return False

    if (maze[x][y] == 1 and check[x][y] == 0):
        print(f'현재 좌표 :     ({x},{y}) ')
        check[x][y] = 1
        dfs(x,y+1,move_count+1)
        dfs(x+1,y,move_count+1)
        dfs(x-1,y,move_count+1)
        dfs(x,y-1,move_count+1)
        return True
    return False

dfs(0,0,1)

print(res)