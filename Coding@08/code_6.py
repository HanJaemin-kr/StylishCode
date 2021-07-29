# 왕실의 나이트
# 8x8 체스판에서 현재 위치에 나이트가 움직일 수 있는 경우의 수를 구하여라


data = input()
row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1
print(row,col)
move = [ (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1,2), (1,-2), (2,1), (2,-1) ]
count = 0

for m in move:
    tmp_r = row + m[0]
    tmp_c = col + m[1]

    if(tmp_r <= 0 or tmp_r >= 8 or tmp_c <= 0 or tmp_c >= 8):
        continue
    print(tmp_r, tmp_c)
    count += 1

print(count)
