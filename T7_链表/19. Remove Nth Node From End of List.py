# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 哨兵返回值，双指针控制距离
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left=right=dummy=ListNode(next=head)
        for _ in range(n):
            right=right.next
        while right.next:
            right=right.next
            left=left.next
        left.next=left.next.next
        return dummy.next