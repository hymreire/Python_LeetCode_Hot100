# 2841. Maximum Sum of Almost Unique Subarray
# 滑动窗口
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        left=0
        ans=0
        s=0 # 累计和
        cnt=defaultdict(int) # 字典
        t=0 # 种类数
        for right,x in enumerate(nums):
            # 入窗
            s+=x
            cnt[x]+=1
            if cnt[x]==1:
                t+=1
            if right-left<k-1: # 窗口长度不足k-1
                continue
            # 更新答案
            if t>=m: # 如果还有额外条件，在窗口形成后判断是否更新答案
                ans=max(ans,s)
            # 出窗
            s-=nums[left]
            cnt[nums[left]]-=1
            if cnt[nums[left]]==0:
                t-=1
            left+=1
        return ans