# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 递归，尾插法
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        rev_head=self.reverseList(head.next) # 向下传递
        tail=head.next
        tail.next=head
        head.next=None
        return rev_head

# 迭代，头插法
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        cur=head
        while cur:
            nxt=cur.next # 中间变量
            cur.next=pre
            pre=cur
            cur=nxt
        return pre