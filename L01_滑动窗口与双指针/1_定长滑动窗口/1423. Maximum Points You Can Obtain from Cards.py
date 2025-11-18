# 1423. Maximum Points You Can Obtain from Cards

# 滑动窗口
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        left,right=-1,n # 待动
        ans=s=0
        for i in range(k): # 可以用sum实现
            left+=1 # 最后到k-1
            s+=cardPoints[i]
        ans=s
        for i in range(k):
            right-=1
            s+=cardPoints[right]-cardPoints[left]
            ans=max(ans,s)
            left-=1
        return ans
# 时间复杂度：O(k)、空间复杂度：O(1)