# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:    return None
        
        even = ListNode('d') 
        odd = ListNode('d')
        
        pointerEven = even
        pointerOdd = odd
        
        isOdd = True
        while head is not None:
            print(head.val)
            if isOdd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            
            isOdd = not isOdd
            head = head.next
        
        even.next = None
        odd.next = pointerEven.next
        
        return pointerOdd.next
