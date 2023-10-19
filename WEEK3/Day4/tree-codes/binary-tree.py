from collections import deque
class BinaryTree:

    def __init__(self, value, left=None, right=None):
        """Creating an instance of BinaryTree with the attributes of:
          Value(Data at current node)
          Left(Pointer to data on the left)
          Right(Pointer to data on the right)"""
        self.value = value
        self.left = left
        self.right = right

    def __str__(self, level=0):
        """as the tree has multiple levels, printing the data for the BinaryTree requires a function:
        leaf_str()
        to be called multiple times.
        In this way, the string method can print the entire tree with all of the left and right branches of each branch from the root to the head of the lowest branch on the left or the right"""

        def leaf_str():
            return '\t' * (level + 1) + 'None\n'
        
        tree_str = '\t' * level + repr(self.value) + '\n'

        for child in [self.left, self.right]:
            tree_str += child.__str__(level+1) if child else leaf_str()

        return tree_str
    
    @staticmethod
    def binary_search(tree, value):
        if tree == None:
            return None
        
        if value == tree.value:
            return tree
        elif value < tree.value:
            return tree.binary_search(tree.left, value)
        else:
            return tree.binary_search(tree.right, value)

    def dfs(self):
        print(self.value)
        if self.left:
            self.left.dfs()
        if self.right:
            self.right.dfs()

    def bfs(self):
        node_queue = deque()
        node_queue.append(self)

        while len(node_queue) > 0:
            current = node_queue.popleft()
            print(current.value)
            if current.left:
                node_queue.append(current.left)
            if current.right:
                node_queue.append(current.right)
    @staticmethod
    def find_in_tree(tree, target):
        if tree == None:
            return None
        
        if tree.value == target:
            return tree
        
        found_left = tree.find_in_tree(tree.left, target)
        found_right = tree.find_in_tree(tree.right, target)

        if found_left:
            return found_left
        elif found_right:
            return found_right
        else:
            return None
        
        
        
    
myTree = BinaryTree(
    56,
    BinaryTree(
        22,
        BinaryTree(10,
                   BinaryTree(20)),
        BinaryTree(30)
    ),
    BinaryTree(
        81,
        BinaryTree(77),
        BinaryTree(22)
    )
)

tree = BinaryTree(
    1,
    BinaryTree(
        2,
        BinaryTree(4),
        BinaryTree(5)
    ),
    BinaryTree(
        3,
    
        BinaryTree(6),
        BinaryTree(7)
    ),
)
# tree.bfs()
# myTree.bfs()
# tree.dfs()
# myTree.dfs()

# print(myTree)
# print(BinaryTree.binary_search(myTree,1))
# print(BinaryTree.find_in_tree(myTree, 56))
# # print(BinaryTree.find_in_tree(myTree, 22))
print(BinaryTree.find_in_tree(myTree, 77))
print(BinaryTree.find_in_tree(myTree, 1000))
