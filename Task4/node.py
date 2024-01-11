class Node:
    def __init__(self, id, left=None, right=None, children=None):
        self.id = id
        self.left = left
        self.right = right
        self.children = children or []
    
    def __repr__(self):
        return "Node {}, left: {}, right: {}, children: {}".format(self.id, self.left, self.right, self.children)