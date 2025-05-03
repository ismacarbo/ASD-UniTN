import pygame

class Player:
    def __init__(self, x, y, maze, tile_size):
        self.x = x
        self.y = y
        self.maze = maze
        self.tile_size = tile_size

    def move(self, dx, dy):
        newX = self.x + dx
        newY = self.y + dy
        if self.maze[newY][newX] != "#":
            self.x = newX
            self.y = newY

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (0, 100, 255),
            pygame.Rect(
                self.x * self.tile_size,
                self.y * self.tile_size,
                self.tile_size,
                self.tile_size
            )
        )
