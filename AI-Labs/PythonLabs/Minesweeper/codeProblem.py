def solve(grid):
    lista = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#':
                lista.append(tuple((i, j)))
            else:
                grid[i][j] = 0
    for i, j in lista:
        if i - 1 >= 0 and grid[i - 1][j] != '#':
            grid[i - 1][j] += 1
        if i + 1 < len(grid) and grid[i + 1][j] != '#':
            grid[i + 1][j] += 1
        if j - 1 >= 0 and grid[i][j - 1] != '#':
            grid[i][j - 1] += 1
        if j + 1 < len(grid) and grid[i][j + 1] != '#':
            grid[i][j + 1] += 1
        if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] != '#':
            grid[i - 1][j - 1] += 1
        if i - 1 >= 0 and j + 1 < len(grid) and grid[i - 1][j + 1] != '#':
            grid[i - 1][j + 1] += 1
        if i + 1 < len(grid) and j - 1 >= 0 and grid[i + 1][j - 1] != '#':
            grid[i + 1][j - 1] += 1
        if i + 1 < len(grid) and j + 1 < len(grid) and grid[i + 1][j + 1] != '#':
            grid[i + 1][j + 1] += 1

    new_grid = ["   ".join(map(str, row)) for row in grid]  # list comprehension
    return new_grid


n = int(input())
minesweeper = []
for _ in range(n):
    minesweeper.append(list(input().split()))
print(*solve(minesweeper), sep='\n')
