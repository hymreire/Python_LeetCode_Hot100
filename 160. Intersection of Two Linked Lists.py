# 160. Intersection of Two Linked Lists

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 核心：x+z+y=y+z+x，所以各自走完然后沿着对方的路走一定能同时达到交点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p,q=headA,headB
        while p is not q:
            p=p.next if p else headB
            q=q.next if q else headA
        return p


# ========== 面试调试用：快速构建链表 ==========（力扣链表的调试还真难写，感觉链表题只能直接背下来。。。）
def build(intersectVal, listA, listB, skipA, skipB):
    """快速构建两个链表"""
    nodesA = [ListNode(x) for x in listA]
    for i in range(len(nodesA)-1):
        nodesA[i].next = nodesA[i+1]
    
    if intersectVal != 0:
        intersect = nodesA[skipA]
        nodesB = [ListNode(x) for x in listB[:skipB]]
        for i in range(len(nodesB)-1):
            nodesB[i].next = nodesB[i+1]
        if nodesB:
            nodesB[-1].next = intersect
            headB = nodesB[0]
        else:
            headB = intersect
    else:
        nodesB = [ListNode(x) for x in listB]
        for i in range(len(nodesB)-1):
            nodesB[i].next = nodesB[i+1]
        headB = nodesB[0] if nodesB else None
    
    return nodesA[0] if nodesA else None, headB

# ========== 快速测试 ==========
if __name__ == "__main__":
    # 示例1: 相交在8
    a1, b1 = build(8, [4,1,8,4,5], [5,6,1,8,4,5], 2, 3)
    res1 = Solution().getIntersectionNode(a1, b1)
    print(f"示例1: {res1.val if res1 else None}")  # 应该输出 8
    
    # 示例2: 相交在2
    a2, b2 = build(2, [1,9,1,2,4], [3,2,4], 3, 1)
    res2 = Solution().getIntersectionNode(a2, b2)
    print(f"示例2: {res2.val if res2 else None}")  # 应该输出 2
    
    # 示例3: 不相交
    a3, b3 = build(0, [2,6,4], [1,5], 3, 2)
    res3 = Solution().getIntersectionNode(a3, b3)
    print(f"示例3: {res3.val if res3 else None}")  # 应该输出 None