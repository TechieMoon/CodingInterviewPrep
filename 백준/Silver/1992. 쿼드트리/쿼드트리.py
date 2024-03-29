def recursive(arr, row, col, len):
    init = arr[row][col]
    for i in range(row, row + len):
        for j in range(col, col + len):
            if arr[i][j] != init:
                half = len // 2
                return '(' + \
                recursive(arr, row, col, half) + \
                recursive(arr, row, col + half, half) + \
                recursive(arr, row + half, col, half) + \
                recursive(arr, row + half, col + half, half) + \
                ')'

    return init

n = int(input())
array = [[0]*n for _ in range(n)]

for i in range(n):
    row = list(input())
    array[i] = row

print(recursive(array,0,0,n))