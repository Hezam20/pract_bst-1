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

    def insert_node_iter(self, node, new_node):
        while node:
            if node.element < new_node.element:
                if not node.right:
                    node.right = new_node
                    return
                node = node.right 
            if not node.left:
                node.left = new_node
                return
            else:
                node = node.left
        return

    def is_found(self, target, rec=False):
        if not self.root:
            return "The tree is empty"
        if rec:
            return self.search_node_rec(self.root, target)
        return self.search_node_iter(self.root, target) 

    def search_node_rec(self, node, target):
        if not node:
            return False 
        if node.element == target:
            return True 
        if node.element < target:
            return self.search_node_rec(node.right, target)
        return self.search_node_rec(node.left, target)

    @staticmethod
    def search_node_iter(node, target):
        while node and node.element != target:
            if node.element < target:
                node = node.right 
            else:
                node = node.left 
        if not node:
            return False 
        return True

    def delete_node(self, target, rec=False):
        if not self.root:
            return "Tree is empty"
        
        if rec:
            self.delete_node_rec(self.root, target)
        else:
            self.delete_node_iter(self.root, target)
        return

    def successor(self, node):
        if node.right.left:
            node.element = node.right.element
            node.right = node.right.right 
            return 
        tmp = node.right 
        while tmp.left.left:
            tmp = tmp.left 
        node.element = tmp.left.element
        tmp.left = tmp.left.right 
        return


    def delete_node_rec(self, node, target):
        if not node:
            return False 
        
        if node.element == target:
            if not node.left and not node.right:
                return None 
            if not node.left or not node.right:
                if node.left:
                    return node.left 
                return node.right
            return self.successor(node)

        parent = node 
        if node.element < target:
            parent.right = self.delete_node_rec(node.right, target)
        else:
            parent.left = self.delete_node_rec(node.left, target)
        return parent 
        
