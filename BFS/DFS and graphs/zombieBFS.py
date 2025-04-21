from collections import deque
import time
import random

ROWS=6
COLS=6

grid = [['#' for _ in range(ROWS)] for _ in range(COLS)]

directionsBuilding = [(0, 2), (0, -2), (2, 0), (-2, 0)]
directions=[(0,1),(0,-1),(1,0),(-1,0)]

#grid = [
 #   ['#', '#', '#', '#', '#'],
 #   ['#', '.', '.', '.', '#'],
   # ['#', '.', '#', '.', '#'],
  #  ['#', 'Z', '.', '.', '#'],
   # ['#', '#', '#', '#', '#']
#]


#grid generated with dfs (not good for testing)
def generateTerrain(x,y):
    grid[y][x]=' '
    dirs=directionsBuilding[:]
    random.shuffle(dirs)
    for dy,dx in dirs: 
        ny,nx=dy+y,dx+x
        if 1 <= ny < ROWS-1 and 1 <= nx < COLS-1:
            if grid[ny][nx]=='#':
                grid[y + dy//2][x + dx//2] = '.'
                generateTerrain(ny, nx)

def addZombies(n):
    added=0
    while added<n:
        y,x=random.randint(1,ROWS-2),random.randint(1,COLS-2)
        if grid[y][x]=='.':
            grid[y][x]='Z'
            added+=1

def printGrid():
    for row in grid:
        print(' '.join(row))
    print()

def infect(grid):
    y,x=0,0
    visited=set()
    queue=deque()

    #map all the zombies pre bfs
    for y in range(ROWS):
        for x in range(COLS):
            if grid[y][x]=="Z":
                queue.append((y,x))
                visited.add((y,x))

    turns=0

    while queue:
        for _ in range(len(queue)): 
            y,x=queue.popleft()     #dequeue current -->
            for dy,dx in directions: #check neighbours
                ny,nx=y+dy,x+dx
                if 0<=ny<ROWS and 0<=nx<COLS:
                    if grid[ny][nx]=='.' and (ny,nx) not in visited and not grid[ny][nx]=="#": #if human and not visited infect (visit the node)
                        grid[ny][nx]='Z'
                        visited.add((ny,nx))
                        queue.append((ny,nx))
        if queue:
            turns+=1
            print(f"levels of infection: {turns}")
            printGrid()
            time.sleep(0.5)


    print(f"all infected in {turns}")


def main():
    generateTerrain(1,1)
    addZombies(2)
    print("initial map: ")
    printGrid()
    infect(grid)

if __name__ == "__main__":
    main()