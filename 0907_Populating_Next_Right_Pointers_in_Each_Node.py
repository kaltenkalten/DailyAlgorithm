"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        import queue

        if root is None:  return None

        q = queue.Queue()

        q.put(root)

        while q.qsize() > 0:
            size = q.qsize()
            pre_node = None
            for _ in range(size):
                node = q.get()
                #print(node.val)
                if pre_node is not None:
                    pre_node.next = node

                if node.left is not None:
                    q.put(node.left)
                    q.put(node.right)

                pre_node = node

            pre_node.next = None


        return root
