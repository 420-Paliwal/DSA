def mat(arr):
    row = len(arr)
    for i in range(1,row):
        for j in range(i):
            arr[j][i], arr[i][j] = arr[i][j], arr[j][i]

    for i in range(row):
        arr[i].reverse()
    return arr

arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print(mat(arr))