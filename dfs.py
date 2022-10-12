class Node:
    def __init__(self,node):
        self.data = None
        self.next = None
    def __str__(self):
        self.node = None
        self.next = None
        self.left = None
        self.right = None

    def push(self):
        self.node = None
        self.left = None
        self.right = None
        self.left.right = None

    def pop(self):
        self.node = None
        self.left.right = None
        self.left.left.right = None
        self.left.right.right = None


push = Node
next.left = (1)
next.left.right = (2)
next.right = (3)
next.right.left = (4)
next.left.right.left=(5)
print("implement the terminal")
