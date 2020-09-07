# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        
        stack = [[root, False]]
        
        while len(stack) > 0:
            node, isVal = stack.pop()
            if node is not None:
                if isVal:
                    #print(node.val)
                    k -= 1
                    if k == 0:
                        return node.val
                    continue
                
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
                
                
        return None
