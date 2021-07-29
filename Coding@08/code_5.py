size = input()
move = input().split()

size = int(size)
res_x = 0
res_y = 0

for i in move:
    mov_x = 0
    mov_y = 0

    if(i == 'L'):
        mov_x -= 1

    elif (i == 'R'):
        mov_x += 1

    elif (i == 'U'):
        mov_y -= 1

    else:
        mov_y += 1

    
    if(res_x + mov_x > size or res_x + mov_x < 0):
        continue
    if(res_y + mov_y > size or res_y + mov_y < 0):
        continue

    res_x += mov_x
    res_y += mov_y

print(res_y,res_x)
