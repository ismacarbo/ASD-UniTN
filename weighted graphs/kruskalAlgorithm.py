import heapq
import random
import math
import matplotlib.pyplot as plt

NUMREIGNS=10
WIDTH=100
HEIGHT=100

class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)] #each node is its own parent
        self.rank=[0]*n #union by rank: avoding random ranking due to efficency
    
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x]) #path compression: future searches more fast
        return self.parent[x]
    
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)

        if root_x==root_y:
            return False #already connected cannot apply union-rank
        
        #choosing rank of parent based on majority
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x]=root_y
        elif self.rank[root_x]>self.rank[root_y]:
            self.parent[root_y]=root_x
        else:
            self.parent[root_y]=root_x
            self.rank[root_x]+=1

        return True


def generateReigns():
    return [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUMREIGNS)]


def createGraph(reigns):
    graph=[]
    n=len(reigns)
    for i in range(n):
        for j in range(i + 1, n):
            distance = math.hypot(reigns[i][0] - reigns[j][0], reigns[i][1] - reigns[j][1]) #euclide's distance
            graph.append((distance, i, j))

    return graph


def kruskal(graph,n):
    dsu=DisjointSet(n)
    mst=[]
    heap=list(graph) #graph=list of (cost,u,v)
    heapq.heapify(heap) #all edges inserted
    totalCost=0

    while heap and len(mst)<(n-1): #till empty and n-1 edge all nodes are connected to a single mst
        cost,u,v=heapq.heappop(heap) 
        if dsu.union(u,v): #if union is possibile
            mst.append((cost,u,v)) #add edge to mst
            totalCost+=cost

    return mst,totalCost

def displayAlliances(mst):
    print("Alliances formed:")
    for cost, u, v in mst:
        print(f"Reign {u} ↔ Reign {v} | Cost: {cost:.2f}")


def plotReigns(reigns, mst, totalCost):
    plt.figure(figsize=(10,10))
    for idx, (x, y) in enumerate(reigns):
        plt.plot(x, y, 'bo')
        plt.text(x + 1, y + 1, f"R{idx}")

    for cost, u, v in mst:
        x1, y1 = reigns[u]
        x2, y2 = reigns[v]
        plt.plot([x1, x2], [y1, y2], 'g-')

    plt.title(f"Kruskal's MST - Total Alliance Cost: {totalCost:.2f}")
    plt.grid(True)
    plt.show()


def main():
    reigns=generateReigns()
    graph=createGraph(reigns)
    mst,cost=kruskal(graph,len(reigns))
    displayAlliances(mst)
    print(f"\nTotal Cost to Unite the Kingdoms: {cost:.2f}")
    plotReigns(reigns,mst,cost)


if __name__=="__main__":
    main()
    