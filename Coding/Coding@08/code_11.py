def setting(data):
    return data[1]


n = int(input())

arr = []
for i in range(n):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))

array = sorted(arr, key = setting)

for i in array:
    print(i[0], end ='')
