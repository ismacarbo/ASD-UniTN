import pygame
import heapq

class Enemy: 
    def __init__(self,x,y,maze,tile_size):
        self.x=x
        self.y=y
        self.maze=maze
        self.path=[]
        self.tile_size=tile_size

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
    
    def findPath(self,start,goal):
        visited=[]
        heapq.heappush(visited,(0,start))
        cameFrom={start:None}

        gScore={start: 0}

        while visited:
            _,current=heapq.heappop(visited)
            if current==goal:
                break

            for neighbor in self.neighbors(current):
                tentativeG=gScore[current]+1
                if tentativeG<gScore.get(neighbor, float('inf')):
                    cameFrom[neighbor]=current
                    gScore[neighbor]=tentativeG
                    priority=tentativeG+self.heuristic(goal,neighbor)
                    heapq.heappush(visited,(priority,neighbor))

        #reconstruct path
        path = []
        curr = goal
        while curr != start:
            if curr not in cameFrom:
                return []
            path.append(curr)
            curr = cameFrom[curr]
        path.reverse()
        return path

    def update(self, player_pos):
            if (self.x, self.y) == player_pos:
                return  #player reached

            if not self.path or self.path[-1] != player_pos:
                self.path = self.findPath((self.x, self.y), player_pos)

            if self.path:
                next_x, next_y = self.path.pop(0)
                self.x, self.y = next_x, next_y

    def draw(self, screen):
            pygame.draw.rect(
                screen,
                (255, 50, 50),
                pygame.Rect(
                    self.x * self.tile_size,
                    self.y * self.tile_size,
                    self.tile_size,
                    self.tile_size
                )
            )
