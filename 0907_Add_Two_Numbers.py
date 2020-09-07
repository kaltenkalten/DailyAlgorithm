# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:    return l1 or l2
        
        cur1 = l1
        cur2 = l2
        flag = 0
        
        while cur1.next is not None and cur2.next is not None:
            cur1.val += flag + cur2.val
            flag = cur1.val // 10
            cur1.val = cur1.val % 10
            
            cur1 = cur1.next
            cur2 = cur2.next
            
           
        if cur1.next is None and cur2.next is not None:
            cur1.next = cur2.next
        
        cur1.val += cur2.val 
        pre_cur1 = None
        
        while cur1 is not None:
            cur1.val += flag
            flag = cur1.val // 10
            cur1.val = cur1.val % 10
            pre_cur1 = cur1
            cur1 = cur1.next
    
        if flag == 1:
            pre_cur1.next = ListNode(1)
            flag = 0
        
        return l1    
            
            
            
            
