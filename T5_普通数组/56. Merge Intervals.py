# 56. Merge Intervals

# 排序+贪心
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort(key=lambda q:q[0])
        for p in intervals:
            if ans and p[0]<=ans[-1][1]:
                ans[-1][1]=max(p[1],ans[-1][1])
            else:
                ans.append(p)
        return ans