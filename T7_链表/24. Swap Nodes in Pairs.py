# 24. Swap Nodes in Pairs

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 迭代，哨兵返回值，四个节点控制链表流向
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h0=dummy=ListNode(next=head)
        h1=head
        while h1 and h1.next:
            h2=h1.next
            h3=h2.next
            h0.next=h2
            h2.next=h1
            h1.next=h3
            h0=h1
            h1=h3
        return dummy.next

# 递归，三个节点控制链表流向
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        h1=head
        h2=h1.next
        h3=h2.next
        h1.next=self.swapPairs(h3)
        h2.next=h1
        return h2