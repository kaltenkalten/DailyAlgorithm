# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        if headA is None or headB is None:  return None
        
        curA = headA
        curB = headB
        isOnceA = True
        isOnceB = True
        
        while curA is not None and curB is not None:
            #print(curA, curB)
            if curA == curB:
                #print(curA, curB)
                return curA
            
            curA = curA.next
            curB = curB.next
            
            if curA is None and isOnceA:
                curA = headB
                isOnceA = False
            if curB is None and isOnceB:
                curB = headA
                isOnceB = False
        
        return None
                
            
