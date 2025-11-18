# 2379. Minimum Recolors to Get K Consecutive Black Blocks

# 滑动窗口
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans=inf
        tmp=0
        left=0
        for right,c in enumerate(blocks):
            tmp+=1 if c=='W' else 0
            if right-left<k-1:
                continue
            ans=min(ans,tmp)
            tmp-=1 if blocks[left]=='W' else 0
            left+=1
        return ans

# 时间复杂度：O(n)、空间复杂度：O(1)