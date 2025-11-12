# 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset=set(nums)
        ans=0
        for x in nset:
            if x-1 in nset:
                continue # 强制找到一个最小起点
            y=x+1
            while y in nset:
                y+=1
            ans=max(ans,y-x) # 极端情况：x+1都没有时，x长度为1，程序满足条件
        return ans

# 早停优化
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        nset=set(nums)
        l=len(nset)
        for x in nset:
            if x-1 in nset:
                continue
            y=x+1
            while y in nset:
                y+=1
            ans=max(ans,y-x)
            if ans*2>=l: # 早停
                break
        return ans