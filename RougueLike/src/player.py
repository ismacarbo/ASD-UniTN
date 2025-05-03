import pygame

TILE_SIZE=5

class Player: 
    def __init__(self,x,y,maze):
        self.x=x
        self.y=y
        self.maze=maze #to know where the walls are

    def move(self,dx,dy):
        newX=self.x+dx
        newY=self.y+dy

        if self.maze[newX][newY]!="#":
            newX=self.x
            newY=self.y

    def draw(self, screen):
        pygame.draw.rect(
            screen, (0, 100, 255),
            pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )