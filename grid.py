t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    grid = []
    for i in range(n):
        row = ''.join(sorted(input().strip()))
        grid.append(row)

    ok = True

    for col in range(len(grid[0])):
        for row in range(1, n):
            if grid[row][col] < grid[row-1][col]:
                ok = False
                break
        if not ok:
            break

    print("YES" if ok else "NO")
