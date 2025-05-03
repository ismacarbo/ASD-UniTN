import random
import player

#mod: inserted by user
WIDTH=60
HEIGHT=30
NUM_ROOMS=10
MIN_SIZE=4
MAX_SIZE=8

class Room:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.cx=x+h
        self.cy=y+h #centroids

    def intersects(self, other):
     return (self.x < other.x + other.w and
            self.x + self.w > other.x and
            self.y < other.y + other.h and
            self.y + self.h > other.y)

class UnionFind:
    def __init__(self,n):
       self.parent=list(range(n))

    def find(self,x):
        while x!=self.parent[x]:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x
    
    def union(self,a,b):
       ra,rb=self.find(a),self.find(b)
       if ra==rb:
          return False
       return True
    
def generateMatrix():
   return [["#" for _ in range(WIDTH)] for _ in range(HEIGHT)]

#creating square rooms then link them with kruskal & union find
def createRooms():
    rooms = []
    attempts = 0
    while len(rooms) < NUM_ROOMS and attempts < 1000:
        w = random.randint(MIN_SIZE, MAX_SIZE)
        h = random.randint(MIN_SIZE, MAX_SIZE)
        x = random.randint(1, WIDTH - w - 2)
        y = random.randint(1, HEIGHT - h - 2)
        new_room = Room(x, y, w, h)

        if all(not new_room.intersects(other) for other in rooms):
            rooms.append(new_room)
        attempts += 1
    return rooms

def dig_room(maze, room):
    for i in range(room.y, room.y + room.h):
        for j in range(room.x, room.x + room.w):
            maze[i][j] = ' '

#creating all the corridors
def dig_corridor(maze, x1, y1, x2, y2):
    if random.choice([True, False]):
        dig_horiz(maze, x1, x2, y1)
        dig_vert(maze, y1, y2, x2)
    else:
        dig_vert(maze, y1, y2, x1)
        dig_horiz(maze, x1, x2, y2)

def dig_horiz(maze, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2)+1):
        maze[y][x] = ' '

def dig_vert(maze, y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2)+1):
        maze[y][x] = ' '


#kruskal algorithm with manhattan distance
def connectRooms(maze,rooms):
    edges=[]
    #inserting all the edges tracked with distance 
    for i in range(len(rooms)):
        for j in range(i+1,len(rooms)):
            distance=abs(rooms[i].cx-rooms[j].cx)+abs(rooms[i].cy-rooms[j].cy)
            edges.append((distance,i,j)) #appending tuples with distance, node1, node2 
    edges.sort() #simulates priority queue because sorting means minor distance in first cell of edges

    #starting unionFind object in order to find if vertex are in the same set(means cycles), if not create a corridor
    uf=UnionFind(len(rooms))
    for d,i,j in edges:
        if uf.union(i,j):
            dig_corridor(maze,rooms[i].cx,rooms[i].cy,rooms[j].cx,rooms[j].cy)


def printMaze(maze):
    for row in maze:
        print("".join(row))


def generate_dungeon():
    maze=generateMatrix()
    rooms=createRooms()
    for room in rooms:
        dig_room(maze,room)
    
    connectRooms(maze,rooms)
    return maze,rooms


if __name__=="__main__":
    maze=generate_dungeon()
    printMaze(maze)
    