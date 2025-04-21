import heapq

grid = [
    ['S', '.', '~', '.', '.'],
    ['#', '#', '.', '#', '~'],
    ['.', '~', '.', '~', 'E'],
    ['.', '.', '.', '.', '#'],
    ['~', '#', '~', '.', '.']
]

#explaining costs in the grid
cost_map = {
    'S': 0,
    '.': 1,
    '~': 2,
    '#': float('inf'),
    'E': 1 
}

ROWS=len(grid)
COLS=len(grid[0])
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def findStartEnd():
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 'S':
                start = (j, i)
            elif grid[i][j] == 'E':
                end = (j, i)
    return start, end


def dijkstra():
    start,end=findStartEnd()
    visited=set()
    distance=[[float('inf')] * COLS for _ in range(ROWS)]
    heap=[]
    heapq.heappush(heap,(0,start)) #insert the start
    while heap:
        cost, (x,y)=heapq.heappop(heap) #pop current vertex with cost
        if (x,y)==end: #end reached
            return cost
        
        if (x,y) not in visited:
            visited.add((x,y))
        
            for dx,dy in directions:
                ny,nx=dy+y,dx+x
                if 0 <= nx < COLS and 0 <= ny < ROWS:
                    if (nx,ny) not in visited:
                        terrain=grid[ny][nx]
                        moveCost=cost_map[terrain]
                        if moveCost==float('inf'):
                            continue #wall so ignore it

                        newCost=moveCost+cost
                        if newCost<distance[ny][nx]:
                            distance[ny][nx]=newCost
                            heapq.heappush(heap,(newCost,(nx,ny))) #inserting newcost and newvertex in heap
    return -1


def main():
    minCost=dijkstra()
    print(f"min cost is: {minCost}")

if __name__ == "__main__":
    main()