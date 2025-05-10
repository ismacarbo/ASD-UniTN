class Inventory:
    def __init__(self,capacity):
        self.capacity=capacity
        self.items=[]

    def currentWeigth(self):
        return sum(item.weigth for item in self.items)
    
    def canAdd(self,item):
        return self.currentWeigth()+item.weigth<=self.capacity
    
    def addItem(self,item):
        if self.canAdd(item):
            self.items.append(item)
            return True
        return False
    
    def __str__(self):
        return "\n".join(str(item) for item in self.items) if self.items else "Inventory is empty."