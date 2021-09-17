class Node:
    def __init__(self, element):
        self.element = element 
        self.left = None 
        self.right = None 


class BST:
    def __init__(self):
        self.root = None 

    def insert_node(self, element, rec=False):
        new_node = Node(element)
        if not self.root:
            self.root = new_node 
        elif rec:
            self.insert_node_rec(self.root, new_node)
        else:
            self.insert_node_iter(self.root, new_node)
        return

    def insert_node_rec(self, node, new_node):
        if node.element < new_node.element:
            if not node.right:
                node.right = new_node 
            else:
                self.insert_node_rec(node.right, new_node)
        else:
            if node.left:
                node.left = new_node 
            else: 
                self.insert_node_rec(node.left, new_node)
        return 