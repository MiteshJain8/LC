# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        node, rnode = head, res
        s = set(nums)
        while node:
            if node.val not in s:
                nnode = ListNode()
                rnode.next = nnode
                rnode = rnode.next
                rnode.val = node.val
            node = node.next
        return res.next