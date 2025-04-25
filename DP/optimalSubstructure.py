import heapq
import random
import math
import matplotlib.pyplot as plt

#redefining reigns minigame with knapsack like problem
#having extra alliances for every of that you have: 
#cost (for manteining it)
#profit with limited gold budget
#goal: choose bonus alliences for maximazing total benefit without surpass the budget


BUDGET=7
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


def plotReigns(reigns, mst, totalCost, bonus_alliances=None):
    plt.figure(figsize=(10,10))

    #reigns plot
    for idx, (x, y) in enumerate(reigns):
        plt.plot(x, y, 'ro')  
        plt.text(x + 1, y + 1, f"R{idx}")

    plotted_mst = False
    plotted_bonus = False

    for cost, u, v in mst:
        plt.plot([reigns[u][0], reigns[v][0]], [reigns[u][1], reigns[v][1]],
                 'g-', label='MST Alliance' if not plotted_mst else "")
        plotted_mst = True


    if bonus_alliances:
        for alliance in bonus_alliances:
            u = alliance['u']
            v = alliance['v']
            plt.plot([reigns[u][0], reigns[v][0]], [reigns[u][1], reigns[v][1]],
                     'c--', linewidth=2, label='Bonus Alliance' if not plotted_bonus else "")
            plotted_bonus = True

    plt.title(f"Kruskal's MST - Cost: {totalCost:.2f} + Bonus Alliances")
    plt.legend()
    plt.grid(True)
    plt.show()


def maximizeBenefits(alliances,budget):
    n=len(alliances) #number of alliances (objects in knapsack)
    dp = [[0] * (budget + 1) for _ in range(n + 1)] #maxinum capacity

    for i in range(1,n+1):
        cost=alliances[i-1]["cost"]  
        benefit=alliances[i-1]["benefit"]
        for j in range(budget+1):
            if cost > j: #alliance costs too much for the actual budget?
                dp[i][j]=dp[i-1][j] #cannot take this alliance (too much cost)
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-cost]+benefit) #best solution? max of not taken or taken (diff the cost from benefit and adding the benefits from that alliance)

    return dp[n][budget],dp

def recostructSolution(alliances,dp,budget):
    i=len(alliances)
    chosen=[]
    b=budget

    while i>0 and b>0:
        if dp[i][b]!=dp[i-1][b]: #checking if dp is changed from this alliance
            chosen.append(alliances[i-1])
            b-=alliances[i-1]["cost"] #updating current budget with diff the current cost
        i-=1
    
    return chosen[::-1]


def generateRandomAlliances(reigns, mst_edges, num_bonus=15):
    n = len(reigns)
    mst_set = set((min(u, v), max(u, v)) for _, u, v in mst_edges)
    bonus_alliances = []

    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in mst_set:
                x1, y1 = reigns[i]
                x2, y2 = reigns[j]
                dist = math.hypot(x1 - x2, y1 - y2)
                cost = max(1, int(dist / 10)) #cost based on distance
                benefit = random.randint(1, 10)  #random benefit
                bonus_alliances.append({'u': i, 'v': j, 'cost': cost, 'benefit': benefit})

    random.shuffle(bonus_alliances)
    return bonus_alliances[:num_bonus]


def main():
    reigns=generateReigns()
    graph=createGraph(reigns)
    mst,cost=kruskal(graph,len(reigns))
    displayAlliances(mst)
    print(f"\nTotal Cost to Unite the Kingdoms: {cost:.2f}")
    bonusAlliances=generateRandomAlliances(reigns,mst)
    max_benefit, dp_table = maximizeBenefits(bonusAlliances, BUDGET)
    chosen = recostructSolution(bonusAlliances, dp_table, BUDGET)

    print(f"\nMaximized Benefit with Bonus Alliances: {max_benefit}")
    print("Chosen Bonus Alliances:")
    for alliance in chosen:
        print(f"Reign {alliance['u']} ↔ Reign {alliance['v']} | Cost: {alliance['cost']} | Benefit: {alliance['benefit']}")
    plotReigns(reigns,mst,cost,bonusAlliances)


if __name__=="__main__":
    main()
    