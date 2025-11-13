# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        cnt=Counter(nums)
        maxcnt=max(cnt.values())
        buckets=[[] for _ in range(maxcnt+1)] # 相同频率值放在同一个桶中
        for x,c in cnt.items():
            buckets[c].append(x)
        for bucket in reversed(buckets):
            ans+=bucket
            if len(ans)==k:
                return ans