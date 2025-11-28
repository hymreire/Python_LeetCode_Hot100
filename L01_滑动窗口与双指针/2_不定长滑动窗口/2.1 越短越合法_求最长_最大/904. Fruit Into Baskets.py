# 904. Fruit Into Baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans=left=0
        cnt=defaultdict(int)
        for right,enter in enumerate(fruits):
            cnt[enter]+=1
            while len(cnt)>2:
                outer=fruits[left]
                cnt[outer]-=1
                if cnt[outer]==0:
                    del cnt[outer] # 删除键值为0的键
                left+=1
            ans=max(ans,right-left+1)
        return ans
# 时间复杂度O(n)，空间复杂度O(1)【最多3个键值对】