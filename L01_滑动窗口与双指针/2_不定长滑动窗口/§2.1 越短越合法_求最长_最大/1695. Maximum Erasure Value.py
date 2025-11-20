# 1695. Maximum Erasure Value

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans=left=tmp=0
        cnt=defaultdict(int) # 这题用布尔数组或集合set也可以
        for right,num in enumerate(nums):
            cnt[num]+=1
            tmp+=num
            while cnt[num]>1:
                outer=nums[left]
                cnt[outer]-=1
                if cnt[outer]==0:
                    del cnt[outer]
                tmp-=outer
                left+=1
            ans=max(ans,tmp)
        return ans
# 时间复杂度：O(n)、空间复杂度O(n)