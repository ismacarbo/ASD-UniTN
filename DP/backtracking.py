import random
import matplotlib.pyplot as plt

MAP_SIZE = 5
MAX_DEFENSE = 10
MOVES = 6

directions = [(-1,0), (1,0), (0,-1), (0,1)]
validPaths = []

def generateMap():
    return [[random.randint(1, MAX_DEFENSE) for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

def draw_map(terrain, path):
    plt.clf()  
    plt.imshow(terrain, cmap='YlOrRd', origin='upper')

    if path:
        xs, ys = zip(*path)
        plt.plot(ys, xs, marker='o', color='blue', linewidth=2)  

    plt.title("Strategic Expansion in Progress")
    plt.colorbar(label='Defense Level')
    plt.pause(0.3)  

def backtracking(x, y, movesLeft, path, terrain, last_defense_high):
    if movesLeft == 0:
        validPaths.append(list(path))
        return

    for dx, dy in directions: #for every direction from the start poiny
        nx, ny = x + dx, y + dy
        if 0 <= nx < MAP_SIZE and 0 <= ny < MAP_SIZE and (nx, ny) not in path: #if not already in the path
            defense = terrain[nx][ny]
            if last_defense_high and defense >= 7: #cannot enter in reigns with defence higher than 7 twice
                continue  

            #if it's safe
            path.append((nx, ny))  #append the coordinate to the path
            draw_map(terrain, path)  #graphic mapping
            backtracking(nx, ny, movesLeft - 1, path, terrain, defense >= 7) #recursion with -1 move
            path.pop() #real backtracking, entered in that cell than valuating constraints than go back for trying other choices

def printTerrain(terrain):
    print("Territory Map (Defense Levels):")
    for row in terrain:
        print(" ".join(f"{cell:2d}" for cell in row))
    print()

def main():
    terrain = generateMap()
    printTerrain(terrain)

    startX, startY = 2, 2  
    pathMap = [(startX, startY)]

    plt.figure(figsize=(6,6))
    plt.ion()  

    draw_map(terrain, pathMap)  
    backtracking(startX, startY, MOVES, pathMap, terrain, terrain[startX][startY] >= 7)

    plt.ioff()  
    plt.show()

    print(f"Total Valid Expansion Paths Found: {len(validPaths)}")
    if validPaths:
        print("\nExample Path:")
        print(validPaths[0])

if __name__ == "__main__":
    main()
