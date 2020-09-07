# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        inorderArr = []
        
        stack = [[root, False]] #node, isVal
        
        while len(stack) != 0:
            node, isVal = stack.pop()
            if node is not None:
                if isVal:
                    inorderArr.append(node.val)
                    continue
                stack.append([node.right, False])
                stack.append([node, True])
                stack.append([node.left, False])
        
        return inorderArr
        
        
        
        
        """
        treeArr = []
        
        def inorder(node):
            if node is None:    return
            
            inorder(node.left)
            treeArr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        return treeArr
        """
