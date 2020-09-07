# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:  return None
        #print(preorder, inorder)
        root = preorder[0]
        inorderIdx = inorder.index(root)
        
        node = TreeNode(root)
        node.left = self.buildTree(preorder[1:inorderIdx+1], inorder[:inorderIdx])
        node.right = self.buildTree(preorder[inorderIdx+1:], inorder[inorderIdx+1:])
        
        return node
