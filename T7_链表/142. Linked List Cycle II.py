# 142. Linked List Cycle II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法：快慢指针
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast is slow:
                while head is not slow:
                    head=head.next
                    slow=slow.next
                return slow
        return None

# 2b-b=kc——>b=kc
# b-a=kc-a——>(b-a)+a=(kc-a)+a=kc
# 因此再走a步必相遇