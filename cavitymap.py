n = int(input())

grid = []

for i in range(n):
    grid.append(input())

ans = []

for i in range(n):

    row = ""

    for j in range(n):

       
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            row += grid[i][j]

        
        elif (grid[i][j] > grid[i-1][j] and
              grid[i][j] > grid[i+1][j] and
              grid[i][j] > grid[i][j-1] and
              grid[i][j] > grid[i][j+1]):

            row += "X"

        else:
            row += grid[i][j]

    ans.append(row)

for i in ans:
    print(i)
    
    