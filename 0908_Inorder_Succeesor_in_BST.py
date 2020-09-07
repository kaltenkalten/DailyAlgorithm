# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None:    return None
        
        if p.right is not None or p == root:
            node = p.right
            while node is not None and node.left is not None:
                node = node.left
            return node
        
        else:
            node = root
            parents = root
            grand_parents = root
            isLeft = False
            while node is not None:
                if node.val > p.val:
                    grand_parents = node
                    parents = node
                    node = node.left
                    isLeft = True
                elif node.val < p.val:
                    parents = node
                    node = node.right
                    isLeft = False
                else:
                    if isLeft:
                        return parents
                    else:
                        if grand_parents == parents:
                            return None
                        return grand_parents
