# 23. Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 堆排序，优先队列
# 最小堆，这里就是调库，然后用它的弹出最小值的功能
# 后面应该有题目直接实现这个数据结构
ListNode.__lt__=lambda a,b: a.val<b.val # 重载小于号，使得堆可以按照val排序
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=cur=ListNode() # 哨兵节点
        h=[head for head in lists if head]
        heapify(h)
        while h:
            n=heappop(h)
            if n.next:
                heappush(h,n.next)
            cur.next=n
            cur=cur.next
        return dummy.next

# 分治，递归
# 分：拆分中点，治：合并有序链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def m2(self,l1,l2):
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
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m=len(lists)
        if m==0:
            return None
        elif m==1:
            return lists[0]
        else:
            l=self.mergeKLists(lists[:m//2])
            r=self.mergeKLists(lists[m//2:])
        return self.m2(l,r)

# 分治，迭代
# 自底向上，两两合并
class Solution:
    def m2(self,l1,l2):
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
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m=len(lists)
        if m==0:
            return None # 空表返回None
        step=1
        while step<m:
            for i in range(0,m-step,step*2): # 两个为一组，避免越界（至少留step）
                lists[i]=self.m2(lists[i],lists[i+step]) # i和i+step都存在i里
            step*=2
        return lists[0] # 最后所有的值都存在0中

## 一般来讲，递归——>迭代，所以迭代比递归难写
## 建议可以好好背一下这道题的迭代解法，个人认为比上一道题好写多了