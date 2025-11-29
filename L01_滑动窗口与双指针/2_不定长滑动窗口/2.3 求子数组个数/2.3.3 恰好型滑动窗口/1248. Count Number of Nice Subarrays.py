# 1248. Count Number of Nice Subarrays

class Solution:
    def numLeast(self, nums, k): # 恰好k个奇数
        ans=left=cnt=0
        for right,n in enumerate(nums):
            if n%2==1:
                cnt+=1
            while cnt>=k and left<=right:
                if nums[left]%2==1:
                    cnt-=1
                left+=1
            ans+=left
        return ans

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.numLeast(nums,k)-self.numLeast(nums,k+1)
# 时间复杂度：O(n)
# 空间复杂度：O(1)