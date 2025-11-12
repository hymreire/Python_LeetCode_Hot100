# 42. Trapping Rain Water

from typing import List

# 方法1：前后缀分解
class Solution: # 要调试其他方法时只要把这个Solution加个1即可
    def trap(self, height: List[int]) -> int:
        n=len(height)
        ans=0
        pre=[0]*n
        pre[0]=height[0]
        for i in range(1,n):
            pre[i]=max(pre[i-1],height[i])
        bac=[0]*n
        bac[-1]=height[-1]
        for i in range(n-2,-1,-1):
            bac[i]=max(bac[i+1],height[i])
        for i in range(n):
            ans+=(min(pre[i],bac[i])-height[i])
        return ans

# 方法2：相向双指针
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        pre=0
        suf=0
        l,r=0,n-1
        ans=0
        while l<r:
            pre=max(pre,height[l])
            suf=max(suf,height[r])
            if pre<suf:
                ans+=pre-height[l]
                l+=1
            else:
                ans+=suf-height[r]
                r-=1
        return ans

# 方法3：单调栈
class Solution:
    def trap(self, height: List[int]) -> int:
        st=[]
        ans=0
        for i,h in enumerate(height):
            while st and height[st[-1]]<=h: ## 比较高而不是索引
                bottom_h=height[st.pop()]
                if not st:
                    break
                left=st[-1]
                col_h=min(height[left],h)-bottom_h
                ans+=col_h*(i-left-1)
            st.append(i)
        return ans

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print(solution.trap(height))