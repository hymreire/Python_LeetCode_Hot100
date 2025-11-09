# 148. Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 归并排序，分治，分：拆分中点，治：合并有序链表
# 排序链表=拆分中点+合并有序链表
class Solution:
    # 快慢指针拆分中间节点
    def middle(self,head): # 拆分两个链表
        fast=slow=head
        while fast and fast.next: # 必须while
            pre=slow
            fast=fast.next.next
            slow=slow.next
        pre.next=None # 扯断很重要
        return slow
    # 哨兵节点合并有序链表
    def union(self,h1,h2): # 合并有序链表
        dummy=cur=ListNode()
        while h1 and h2:
            if h1.val<=h2.val:
                cur.next=h1
                h1=h1.next
            else:
                cur.next=h2
                h2=h2.next
            cur=cur.next
        cur.next=h1 or h2
        return dummy.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        h1=head
        h2=self.middle(head)
        h1=self.sortList(h1)
        h2=self.sortList(h2)
        return self.union(h1,h2)

# 归并排序，自底向上
# 这个太恶心了，我只能盘一下逻辑，没办法背下来
# 以后有时间再背一下吧
class Solution:
    def getlen(self,head):
        ans=0
        cur=head
        while cur:
            ans+=1
            cur=cur.next
        return ans
    def sp(self,head,size): # 拆分链表：当前链表尾端截断，并返回下一链表的头部
        cur=head
        for _ in range(size-1):
            if cur is None:
                break
            cur=cur.next
        if cur is None or cur.next is None:
            return None
        next_head=cur.next
        cur.next=None
        return next_head
    def me(self,l1,l2):
        cur=dummy=ListNode()
        while l1 and l2:
            if l1.val<=l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 or l2
        while cur.next:
            cur=cur.next # 返回尾节点的值
        return dummy.next,cur
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=self.getlen(head) # 计算链表长度
        dummy=ListNode(next=head) # 哨兵节点
        step=1 # 初始步长
        # 递推：自底向上：每两个合并排序，然后逐渐增大步数，直到全部都排序完毕
        while step<l:
            nt=dummy # 终点
            cur=dummy.next # 起点
            while cur:
                h1=cur
                h2=self.sp(h1,step)
                cur=self.sp(h2,step) # 切割，顺便走到下一轮
                h,t=self.me(h1,h2)
                nt.next=h # 上一尾节点接着这个合并有序链表的头
                nt=t # 尾节点
            step*=2
        return dummy.next