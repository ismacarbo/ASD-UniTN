RED = "RED"
BLACK = "BLACK"

class RBNode:
    def __init__(self, loot, color=RED, parent=None, left=None, right=None):
        self.loot = loot
        self.key = loot.value
        self.color = color
        self.parent = parent
        self.left = left or NIL
        self.right = right or NIL

    def __str__(self):
        return f"{self.loot.name} ({self.key}) [{self.color}]"

class NILNode:
    def __init__(self):
        self.color = BLACK
        self.left = None
        self.right = None
        self.parent = None
        self.key = None

    def __bool__(self):
        return False

NIL = NILNode()

class RedBlackTree:
    def __init__(self):
        self.root = NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, loot):
        node = RBNode(loot)
        y = None
        x = self.root
        while x:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y

        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        node.left = NIL
        node.right = NIL
        node.color = RED
        self.insert_fixup(node)

    def insert_fixup(self, node):
        while node.parent and node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == RED:
                    node.parent.color = BLACK
                    uncle.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)
        self.root.color = BLACK

    def inorder(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node and node != NIL:
            self.inorder(node.left, result)
            result.append(node.loot)
            self.inorder(node.right, result)
        return result

    def search_by_value(self, value):
        node = self.root
        while node and node != NIL:
            if value == node.key:
                return node.loot
            elif value < node.key:
                node = node.left
            else:
                node = node.right
        return None
