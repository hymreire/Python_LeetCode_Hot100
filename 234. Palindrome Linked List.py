# 234. Palindrome Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 回文指针=快慢指针+反转链表
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middle(head): # 快慢指针
            h1=h2=head
            while h2 and h2.next: # 必须选快指针，否则到None之后就没有next了
                h1=h1.next
                h2=h2.next.next
            return h1
        def reverse(head):
            cur=head
            pre=None
            while cur:
                nxt=cur.next
                cur.next=pre
                pre=cur
                cur=nxt
            return pre
        mid=middle(head)
        rev=reverse(mid)
        while(rev):
            if rev.val!=head.val:
                return False
            rev=rev.next
            head=head.next
        return True