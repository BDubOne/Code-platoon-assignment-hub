
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)

    def insert_node(self, current_node, new_node):
        if new_node.value <= current_node.value:
            if current_node.left:
                self.insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.value > current_node.value:
            if current_node.right:
                self.insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node
    
    def find_smallest(self):
        if self.root is None:
            return None
        return self.find_smallest_recursive(self.root)
    
    def find_smallest_recursive(self, current_node):
        if current_node.left is None:
            return current_node.value
        return self.find_smallest_recursive(current_node.left)
tree = BinaryTree()
tree.insert(Node(10))
tree.insert(Node(5))
tree.insert(Node(15))
tree.insert(Node(3))
tree.insert(Node(7))

smallest_value = tree.find_smallest()

print(f" the smallest value in the binary tree is {smallest_value}")

    # find_smallest goes here
