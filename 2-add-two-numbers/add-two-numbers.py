# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tot = 0
        n1, n2 = l1, l2
        head = ListNode()
        cur = head
        carry = 0
        while n1 and n2:
            tot = n1.val + n2.val + carry
            dig = tot % 10
            carry = tot // 10
            cur.next = ListNode(dig)
            cur = cur.next
            n1 = n1.next
            n2 = n2.next
        while n1:
            tot = n1.val + carry
            dig = tot % 10
            carry = tot // 10
            cur.next = ListNode(dig)
            cur = cur.next
            n1 = n1.next
        while n2:
            tot = n2.val + carry
            dig = tot % 10
            carry = tot // 10
            cur.next = ListNode(dig)
            cur = cur.next
            n2 = n2.next
        while carry:
            dig = carry % 10
            carry //= 10
            cur.next = ListNode(dig)
            cur = cur.next

        return head.next