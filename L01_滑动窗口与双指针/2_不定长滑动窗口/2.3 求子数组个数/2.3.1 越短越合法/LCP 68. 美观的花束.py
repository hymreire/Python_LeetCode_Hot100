# LCP 68. 美观的花束

class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        ans=0
        left=0
        rec=defaultdict(int)
        for right,typ in enumerate(flowers):
            rec[typ]+=1
            while rec[typ]>cnt:
                rec[flowers[left]]-=1
                left+=1
            ans+=right-left+1
        return ans

# 时间复杂度：O(n)
# 空间复杂度：O(n)