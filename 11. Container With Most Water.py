# 11. Container With Most Water

# 方法：双指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        n=len(height)
        left,right=0,n-1
        while left<right:
            area=min(height[left],height[right])*(right-left)
            ans=max(ans,area)
            # 左右边谁矮动谁，才有可能得到最大值
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans