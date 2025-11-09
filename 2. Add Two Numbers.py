# 2. Add Two Numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 递归
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode],carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None and carry==0:
            return None
        s=carry
        if l1:
            s+=l1.val
            l1=l1.next
        if l2:
            s+=l2.val
            l2=l2.next
        return ListNode(s%10,self.addTwoNumbers(l1,l2,s//10))

# 递归，原地修改
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode],carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        if l1 is None:
            l1,l2=l2,l1
        s=l1.val+(l2.val if l2 else 0)+carry
        l1.val=s%10
        l1.next=self.addTwoNumbers(l1.next,l2.next if l2 else None,s//10)
        return l1

# 迭代
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur=dummy=ListNode()
        carry=0
        while l1 or l2 or carry:
            s=carry
            if l1:
                s+=l1.val
                l1=l1.next
            if l2:
                s+=l2.val
                l2=l2.next
            cur.next=ListNode(s%10)
            carry=s//10
            cur=cur.next
        return dummy.next