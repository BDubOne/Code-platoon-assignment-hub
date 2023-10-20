# """Binary Search Tree"""

# root = {
#     "val": 5,
#     "left": {
#     "val": 2,
#     "left": {
#         "val": -5,
#         "left": None,
#         "right": None,
#     },
#     "right": {
#     "val": 4,
#     "left": None,
#     "right: None,
#     },
#     "right": {
#         "val": 13,
#         "left: None,
#         "right": None,
#     },

#     }
  
# }

class TreeNode:
    """Binary Tree"""
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        """create a string method that returns the value of a given node with the indexes of its children""" 
        return "val is {self.value}. Left is {self.left}. Right is {self.right}"

    def find_node():
        """Find a particular node based on index"""
        pass
    
    @staticmethod
    def binary_tree_insert(tree,new_value):
        """insert a node based on numbering conventions for sorting into a binary tree. 
        Returns entire tree"""

        new_value = tree.value
        
        if tree is None:
            return tree(new_value)
        
        if new_value < tree.value:
            tree.left = new_value
            print(f'new_val: {new_value} < {tree.value}. Going left')
            if tree.left is None:
                tree.left = new_value
            else:
                return TreeNode.binary_tree_insert(tree.left, new_value)
        else:
            print(f" new_val {new_value} >= {tree.value}. Going right")
            if tree.right is None:
                tree.right = new_value
            else:   
                return TreeNode.binary_tree_insert(tree.right, new_value)

root = TreeNode()

TreeNode.binary_tree_insert(root,50)
TreeNode.binary_tree_insert(root,60)

print(root)
    