grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = set()

def dfs(x, y):
    if (x, y) in visited:
        return
    visited.add((x, y))

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] == 1 and (nx, ny) not in visited:
                dfs(nx, ny)

def count_islands():
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1 and (x, y) not in visited:
                dfs(x, y)
                count += 1
    return count

def main():
    print("number of islands:", count_islands())

if __name__ == "__main__":
    main()
