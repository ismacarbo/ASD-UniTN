import random
import heapq
import math
import matplotlib.pyplot as plt
from collections import defaultdict

NUM_CITIES=10
WIDTH=100
HEIGTH=100

#generate cities randomly
def generateCities():
    return [(random.randint(0,WIDTH),random.randint(0,HEIGTH)) for _ in range(NUM_CITIES)]

#caculate euclide's distance between two cities
def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def primMST(cities):
    visited=set()
    edge=[]
    heap=[]
    n=len(cities)
    totalCost=0
    
    visited.add(0)
    for i in range(1,n): #map the adjacent of start
        heapq.heappush(heap,(distance(cities[0],cities[i]),0,i))

    while len(visited)<n and heap:
        cost,u,v=heapq.heappop(heap)
        if v not in visited:
            visited.add(v)
            edge.append((u,v))
            totalCost+=cost
            for w in range(n): #all non-visited cities remaining push the distance and the edge with weigth
                if w not in visited:  
                    heapq.heappush(heap,(distance(cities[v],cities[w]),v,w))
    
    return edge,totalCost

def plot_map(cities, mst_edges, total_cost, path=None, start=None, goal=None, path_cost=None):
    plt.figure(figsize=(10, 10))

    for idx, (x, y) in enumerate(cities):
        plt.plot(x, y, 'bo', markersize=8)
        plt.text(x + 1.5, y + 1.5, f"C{idx}", fontsize=9, color='black')

    if start is not None:
        plt.plot(cities[start][0], cities[start][1], 'go', markersize=12, label="Start")
    if goal is not None:
        plt.plot(cities[goal][0], cities[goal][1], 'ro', markersize=12, label="Goal")

    for u, v in mst_edges:
        x1, y1 = cities[u]
        x2, y2 = cities[v]
        plt.plot([x1, x2], [y1, y2], 'g-', linewidth=1)

    if path:
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            x1, y1 = cities[u]
            x2, y2 = cities[v]
            plt.plot([x1, x2], [y1, y2], 'r-', linewidth=3, label='A* Path' if i == 0 else "")

    plt.title(f"MST Cost: {total_cost:.2f} | A* Path Cost: {path_cost:.2f}")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()


#heuristic function with euclide distance between cities: minor distance "attract A*  algorithm to avoid unecessary steps"
def make_heuristic(cities):
    def heuristic(a, b):
        return distance(cities[a], cities[b])
    return heuristic


def rebuildPath(cameFrom,current):
    path=[current]
    while current in cameFrom:
        current=cameFrom[current]
        path.append(current)
    return path[::-1] #inverting path

#converting mst to dictionary graph to use A*
def graphFromMST(cities,mstEdges):
    graph=defaultdict(list)
    for u,v in mstEdges:
        d=distance(cities[u],cities[v]) #arch between two cities (MST logic)
        graph[u].append((v,d))
        graph[v].append((u,d))
    return graph

# calculate cost from A* algorithm
def calculate_path_cost(path, cities):
    total = 0
    for i in range(len(path) - 1):
        total += distance(cities[path[i]], cities[path[i+1]])
    return total

def aStar(graph,start,goal,heuristic):
    visited=[]
    heapq.heappush(visited,(0,start))
    cameFrom={} #storing predecessors for building path

    gScore={node: float('inf') for node in graph} #every node filled with infinite
    gScore[start]=0 #calculating score till n from start

    fScore={node: float('inf') for node in graph}
    fScore[start]=heuristic(start,goal) #calculating heuristic in current for future sum g score

    while visited:
        _,current=heapq.heappop(visited) #tuples in visited
        if current==goal:
            return rebuildPath(cameFrom,current)
        
        for neighbor,cost in graph[current]: #every adjacent of current extract neighbor and cost to make a tentative with heuristic
            tentativeG=gScore[current]+cost
            if tentativeG<gScore[neighbor]:
                cameFrom[neighbor]=current
                gScore[neighbor]=tentativeG #tentative added to g score
                fScore[neighbor]=tentativeG+heuristic(neighbor,goal) #summing tentative and heuristic
                heapq.heappush(visited,(fScore[neighbor],neighbor)) #adding in priority queue the fScore with neighbour for leveraging
                #not checking if neighbor is in visited because A* choose always the node with minor fScore
    return None



def main():
    cities = generateCities()
    mst_edges, total_cost = primMST(cities)
    graph = graphFromMST(cities, mst_edges)

    start, goal = 0, NUM_CITIES - 1
    heuristic_func = make_heuristic(cities)
    path = aStar(graph, start, goal, heuristic_func)

    if path:
        cost_path = calculate_path_cost(path, cities)
        print(f"Energy path from C{start} to C{goal}: {path}")
        print(f"MST Total Cost: {total_cost:.2f}")
        print(f"A* Path Cost: {cost_path:.2f}")
    else:
        print("No path found!")

    plot_map(cities, mst_edges, total_cost, path, start, goal, cost_path)


if __name__=="__main__":
    main()