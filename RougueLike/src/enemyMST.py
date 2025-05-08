import pygame
import heapq
from collections import deque

class enemyMST:
    def __init__(self,x,y,maze,tileSize,rooms,mst):
        self.x=x
        self.y=y
        self.maze=maze
        self.tileSize=tileSize
        self.rooms=rooms
        self.mst=mst
        self.path=[]
        self.updateCounter=0
        self.updateRate=20
        self.memoization={}
        self.lastTarget=None

    def draw(self, screen):
        pygame.draw.rect(
            screen, (255, 200, 0),
            pygame.Rect(self.x * self.tileSize, self.y * self.tileSize, self.tileSize, self.tileSize)
        )


    def heuristic(self, a, b):
        #manhattan distance
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
    def neighbors(self, pos):
        x, y = pos
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(self.maze) and 0 <= nx < len(self.maze[0]):
                if self.maze[ny][nx] != "#":
                    yield (nx, ny)

    #using mst to the link from enemy room to my room, using bfs to search the player in the room once reached it
    #using memoization to avoid go to paths already visited
    def findPath(self,start,goal):
        if (start,goal) in self.memoization:
            return list(self.memoization[(start,goal)]) #returning a copy for security
    
        heap=[]
        heapq.heappush(heap,(self.heuristic(start,goal),start)) #(u,v), distance
        cameFrom={start: None}
        visited=set()

        #greedy algorithm: selecting minor cost neighbor in the current position if it doesn't work go back
        while heap:
            _,current=heapq.heappop(heap)
             
            if current==goal:
                break

            if current in visited: #skip to the next node
                continue

            visited.add(current)
            for neigbor in self.neighbors(current):
                if neigbor not in visited:
                    heapq.heappush(heap,(self.heuristic(neigbor,goal),neigbor))
                    if neigbor not in cameFrom:
                        cameFrom[neigbor]=current
            
        #reversing the list fo find correct path 
        path = []
        curr = goal
        while curr != start:
            if curr not in cameFrom:
                return []
            path.append(curr)
            curr = cameFrom[curr]
        path.reverse()
        self.memoization[(start, goal)] = path
        return list(path)
    
    
    #function to check if the player is in the same
    def roomContaining(self,x,y):
        for idx, room in enumerate(self.rooms):
            if room.x <= x < room.x + room.w and room.y <= y < room.y + room.h:
                return idx
        return None

    def pathInMST(self,startRoom,goalRoom):
        adj = {i: [] for i in range(len(self.rooms))}
        for a, b in self.mst:
            adj[a].append(b)
            adj[b].append(a)

        queue=deque([(startRoom,[])])
        visited=set()

        while queue:
            current,path=queue.popleft()
            if current==goalRoom:
                return path+[current]
            if current in visited:
                continue

            visited.add(current)
            for neighbor in adj.get(current,[]):
                queue.append((neighbor,path+[current]))

        return []
    
    def update(self, player_pos):
        # riduci la frequenza di ricalcolo del path
        self.updateCounter += 1
        if self.updateCounter < self.updateRate:
            return
        self.updateCounter = 0

        # 1) se ho già un percorso, muoviti di un passo e torna
        if self.path:
            next_x, next_y = self.path.pop(0)
            self.x, self.y = next_x, next_y
            return

        # 2) individua in quale stanza sono il giocatore e io
        player_room = self.roomContaining(player_pos[0], player_pos[1])
        my_room     = self.roomContaining(self.x, self.y)

        #regenerate the path even in a corridor
        if my_room is None and self.lastTarget is not None:
            new_path = self.findPath((self.x, self.y), self.lastTarget)
            if new_path:
                self.path = new_path
            return

        #if the player room wasn't found nothing to do
        if player_room is None:
            return

        #same room, follow the player
        if my_room == player_room:
            if player_pos != self.lastTarget:
                self.path        = self.findPath((self.x, self.y), player_pos)
                self.lastTarget = player_pos

        #different rooms use mst to choose the path
        else:
            mst_path = self.pathInMST(my_room, player_room)
            if not mst_path:
                return
            next_idx = mst_path[1] if len(mst_path) > 1 else mst_path[0]
            target   = (self.rooms[next_idx].cx, self.rooms[next_idx].cy)
            if target != self.lastTarget:
                self.path        = self.findPath((self.x, self.y), target)
                self.lastTarget = target