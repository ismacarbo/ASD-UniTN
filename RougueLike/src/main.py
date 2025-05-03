import pygame
from map import generate_dungeon

TILE_SIZE = 16  # Ogni cella è 16x16 pixel
FPS = 60

def draw_maze(screen, maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = (0, 0, 0) if cell == "#" else (200, 200, 200)
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color, rect)

def main():
    maze = generate_dungeon()
    WIDTH = len(maze[0])
    HEIGHT = len(maze)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH * TILE_SIZE, HEIGHT * TILE_SIZE))
    pygame.display.set_caption("Roguelike Dungeon")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))
        draw_maze(screen, maze)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
