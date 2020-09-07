# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:    return []
        
        import queue
        
        q = queue.Queue()
        q.put(root)
        
        zigzagLevel = []
        
        while q.qsize() > 0:
            size = q.qsize()
            #level = len(zigzagLevel)
            tmpArr = []
            for _ in range(size):
                node = q.get()
                tmpArr.append(node.val)
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            if len(zigzagLevel) % 2 == 0:
                zigzagLevel.append(tmpArr)
            else:
                zigzagLevel.append(tmpArr[::-1])
                
        return zigzagLevel
