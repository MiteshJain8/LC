# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        while head:
            prev = res
            cur = res.next
            while cur and head.val > cur.val:
                prev = cur
                cur = cur.next

            prev.next = ListNode(head.val)
            prev.next.next = cur
            head = head.next
            
        return res.next
            