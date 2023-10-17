#this is a Page for examples of Python tips for O(log(n))

#Binary Tree

# from .binary_tree import myTree  ---possibly outdated?


# def binary_search(tree, value):
#     # if we call BinarySearch on an empty tree (which we will do in recursive cases) return None
#     if tree == None:
#         return None

#     if value == tree.value:
#         return tree
#     elif value < tree.value:
#         return binary_search(tree.left, value)
#     else:
#         return binary_search(tree.right, value)


# print(binary_search(myTree, 1))


###Binary Tree from https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm#:~:text=To%20insert%20into%20a%20tree,used%20to%20print%20the%20tree.

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    #Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

            else:
                self.data = data
    #Print the Tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()
      
    

    #In order traversal
    # Left --> Root --> Right
    def in_order_traversal(self, root):
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.data)
            res = res + self.in_order_traversal(root.right)
        return res
    
    def pre_order_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order_traversal(root.left)
            res = res + self.pre_order_traversal(root.right)
        return res
    
    # POST ORDER TRAVERSAL !!!!
    def post_order_traversal(self, root):
        res = []
        if root:
            res = self.post_order_traversal(root.left)
            res = res + self.post_order_traversal(root.right)
            res.append(root.data)
        return res
root = Node(12)

root.insert(6)
root.insert(14)
root.insert(3)
root.insert(9)
root.print_tree()
print(root.in_order_traversal(root))
print(root.pre_order_traversal(root))
print(root.post_order_traversal(root))