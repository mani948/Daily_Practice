m, n, r = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(m)]

layers = min(m, n) // 2

for layer in range(layers):

    arr = []

    top = layer
    left = layer
    bottom = m - layer - 1
    right = n - layer - 1


    for j in range(left, right + 1):
        arr.append(mat[top][j])

 
    for i in range(top + 1, bottom):
        arr.append(mat[i][right])


    for j in range(right, left - 1, -1):
        arr.append(mat[bottom][j])


    for i in range(bottom - 1, top, -1):
        arr.append(mat[i][left])

    k = r % len(arr)

    rotated = arr[k:] + arr[:k]

    idx = 0


    for j in range(left, right + 1):
        mat[top][j] = rotated[idx]
        idx += 1

    
    for i in range(top + 1, bottom):
        mat[i][right] = rotated[idx]
        idx += 1

    
    for j in range(right, left - 1, -1):
        mat[bottom][j] = rotated[idx]
        idx += 1

    
    for i in range(bottom - 1, top, -1):
        mat[i][left] = rotated[idx]
        idx += 1

for row in mat:
    print(*row)