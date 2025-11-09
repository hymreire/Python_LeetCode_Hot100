# 25. Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# K个反转=反转链表+两个反转
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0 # 链表长度
        cur=head
        while cur:
            n+=1
            cur=cur.next
        p0=dummy=ListNode(next=head)
        pre=None
        cur=head
        while n>=k:
            n-=k
            for _ in range(k):
                nxt=cur.next
                cur.next=pre # 后对前
                pre=cur
                cur=nxt
            nxt=p0.next
            nxt.next=cur
            p0.next=pre # 尾对头
            p0=nxt
        return dummy.next