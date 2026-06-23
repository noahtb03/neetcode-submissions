# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next   # save where to go next
            current.next = previous    # reverse the pointer
            previous = current         # move previous forward
            current = next_node        # move current forward

        return previous
