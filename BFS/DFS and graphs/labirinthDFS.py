import random

WIDTH=10
HEIGHT=10
PLAYER='X'

maze=[['#' for _ in range(WIDTH)] for _ in range(HEIGHT)]
directions=[(0,2),(0,-2),(2,0),(-2,0)] #two moves for passing walls
currentPosition=[(0,1)]
visited=set()

def generateTerrain(x,y):
    maze[y][x]=' '
    dirs=directions[:] #copy the list for the shuffle
    random.shuffle(dirs)

    for dx, dy in dirs:
        nx, ny=dx+x, y+dy
        if 1<=nx<=WIDTH-1 and 1<=ny<=HEIGHT-1:
            if maze[ny][nx]=='#': #if there's a wall remove it while traversing with dfs (substitute of visited)
                maze[y + dy//2][x + dx//2] = ' '
                generateTerrain(nx,ny)

def printMaze():
    for row in maze:
        print(' '.join(row))

def takeInput():
    move = input("Move (WASD): ").lower()
    if move == 'w':
        return (-1,  0)
    elif move == 's':
        return (1,  0)
    elif move == 'd':
        return (0,  1)
    elif move == 'a':
        return (0, -1)
    else:
        return (0, 0)

def checks(x,y):
    return maze[y][x]!='#'


def traversingDFS(x,y,visited):
    if (x,y) in visited:
        return
    
    if maze[y][x]=='E':
        print(f"found exit in {y},{x}")
        return
    
    visited.add((x,y))
    directions=[(0,1),(0,-1),(1,0),(-1,0)]
    for dx,dy in directions: #checking neighbours
        nx,ny=x+dx,y+dy
        if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
            if not (nx,ny) in visited and maze[ny][nx] in (' ','E'): #if there's no walls and neighbour not visited
                traversingDFS(nx,ny,visited)


def game():
    y, x = 1, 0
    maze[y][x] = PLAYER

    while True:
        printMaze()
        dy, dx = takeInput()
        new_y, new_x = y + dy, x + dx

        if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and checks(new_x,new_y):
            if maze[y][x] != 'S':
                maze[y][x] = ' ' 
            y, x = new_y, new_x
            if maze[y][x] == 'E':
                maze[y][x] = PLAYER
                printMaze()
                print("You won!")
                break
            maze[y][x] = PLAYER
        else:
            print("you hitted a wall!")
                

def main():
    generateTerrain(1,1)
    maze[1][0]='S'
    maze[HEIGHT-2][WIDTH-2]='E'
    traversingDFS(0,1,visited)
    print("/nnow you play:")
    printMaze()
    game()



if __name__ == "__main__":
    main()