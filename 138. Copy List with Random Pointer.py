# 138. Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 交错链表
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        cur=head
        while cur:
            cur.next=Node(cur.val,next=cur.next)
            cur=cur.next.next # 走两步
        cur=head
        while cur:
            if cur.random:
                cur.next.random=cur.random.next # random就是一个指针，因此新表random指向旧表random的next
            cur=cur.next.next # 走两步
        cur=head.next
        while cur.next: # 下家空则结束
            cur.next=cur.next.next
            cur=cur.next
        return head.next