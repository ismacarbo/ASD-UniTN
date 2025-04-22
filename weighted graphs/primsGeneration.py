import random
import heapq
import math
import matplotlib.pyplot as plt

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

def plot_map(cities, mst_edges, total_cost):
    plt.figure(figsize=(8, 8))
    for x, y in cities:
        plt.plot(x, y, 'bo') #blue dot: city

    for u, v in mst_edges:
        x1, y1 = cities[u]
        x2, y2 = cities[v]
        plt.plot([x1, x2], [y1, y2], 'g-') #edge

    plt.title(f"MST between cities - total cost: {total_cost:.2f}")
    plt.grid(True)
    plt.axis('equal')
    plt.show()




def main():
    cities=generateCities()
    mst,totalCost=primMST(cities)
    plot_map(cities, mst, totalCost)

if __name__=="__main__":
    main()