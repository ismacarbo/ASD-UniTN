import pygame
from map import *
from player import Player
from enemy import Enemy
from enemyMST import enemyMST

TILE_SIZE = 16 
FPS = 60

def draw_maze(screen, maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            color = (0, 0, 0) if cell == "#" else (200, 200, 200)
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color, rect)

def main():
    maze, rooms,mst = generate_dungeon()
    #spawning player in the center of the map
    spawn_room = rooms[0]
    x, y = spawn_room.cx, spawn_room.cy
    player = Player(x, y, maze, TILE_SIZE)
    enemy = Enemy(rooms[-1].cx, rooms[-1].cy, maze,TILE_SIZE) #enemy spawn far from player
    enemy_mst_greedy = enemyMST(rooms[3].cx, rooms[3].cy, maze, TILE_SIZE, rooms, mst)


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
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    player.move(0, -1)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    player.move(0, 1)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    player.move(-1, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    player.move(1, 0)

        screen.fill((30, 30, 30))
        draw_maze(screen, maze)
        player.draw(screen)
        enemy.update((player.x, player.y))
        enemy.draw(screen)
        enemy_mst_greedy.update((player.x, player.y))
        enemy_mst_greedy.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
