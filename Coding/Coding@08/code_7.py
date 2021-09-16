#게임 개발
# 막혀있는 칸(1)을 생각해서 가는 방법으로 방문한 칸수 출
row, col = map(int, input().split())
cur_x , cur_y, direction = map(int, input().split())
location = []
for i in range(row):
    location.append(list(map(int, input().split()))) ###

nx = [ 0, 1, 0, -1 ]
ny = [ 1, 0, -1, 0 ]
check = [ [0 for c in range(col)] for r in range(row)]
check[cur_x][cur_y] = 1 


count = 1
fault_count = 0

while True:
    
    cur_direction = direction % 4
    tmp_x = nx[cur_direction] + cur_x
    tmp_y = ny[cur_direction] + cur_y

    if( location[tmp_x][tmp_y] == 0 and check[tmp_x][tmp_y] == 0):
        cur_x = tmp_x
        cur_y = tmp_y
        count += 1
        fault_count = 0
        check[tmp_x][tmp_y] = 1
        print("성ㄱ)현재 방향{} 좌표({},{}) 시도ㅓ 회수: {}".format(cur_direction, tmp_x, tmp_y , fault_count))
        continue

    direction += 1  
    fault_count += 1

    if (fault_count > 4 ):
        tmp_x = cur_x - nx[cur_direction] 
        tmp_y = cur_y - ny[cur_direction]
        if( location[tmp_x][tmp_y] == 0 ):
            cur_x = tmp_x
            cur_y = tmp_y
            fault_count = 0
            print("go to the back 방향{} 좌표({},{}) 시도ㅓ 회수: {}".format(cur_direction, tmp_x, tmp_y, fault_count))
        else:
            break

    print("(ㄱ시ㄹ패)현재 방향{} 좌표({},{}) 시도ㅓ 회수: {}".format(cur_direction, tmp_x, tmp_y , fault_count))

print(count)
