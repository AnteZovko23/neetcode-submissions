# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        initial = ListNode()
        head = initial

        curr = list1
        curr2 = list2

        while curr and curr2:
            if curr.val < curr2.val:
                initial.next = curr
                curr = curr.next
                initial = initial.next
            
            else:
                initial.next = curr2
                curr2 = curr2.next
                initial = initial.next

        if curr:
            while curr:
                initial.next = curr
                curr = curr.next
                initial = initial.next
        
        if curr2:
            while curr2:
                initial.next = curr2
                curr2 = curr2.next
                initial = initial.next


        return head.next