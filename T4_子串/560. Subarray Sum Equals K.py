# 560. Subarray Sum Equals K

from typing import List
from collections import defaultdict

# 方法：前缀和+哈希表

# 写法1：两次遍历
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        n=len(nums)
        pre=[0]*(n+1)
        for i in range(n):
            pre[i+1]=pre[i]+nums[i]
        cnt=defaultdict(int)
        for s in pre: # 遍历前缀和
            ans+=cnt[s-k] # 去找哈希表里是否已经存储了pre-k这个值
            cnt[s]+=1 # 存储当前前缀
        return ans

# 写法2：一次遍历
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre=0 # 前缀和改为缓存变量
        cnt=defaultdict(int) # 哈希表仍然需要
        ans=0
        cnt[0]=1 # 初始化：前缀和为0的子数组有1个（空数组）
        for i,x in enumerate(nums):
            pre+=x
            ans+=cnt[pre-k] # 计算的是pre1-pre0=k，所以顺序不能反！
            cnt[pre]+=1
        return ans

# 写法3：一次遍历
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre=0
        ans=0
        cnt=defaultdict(int)
        for i,x in enumerate(nums):
            cnt[pre]+=1
            pre+=x
            ans+=cnt[pre-k]
        return ans

if __name__ == "__main__":
    solution = Solution()
    # 测试用例2：输入 nums = [1,2,1,2,1], k = 3
    nums = [1,2,1,2,1]
    k = 3
    output = solution.subarraySum(nums, k)
    print("输出:", output)
    print("预期结果: 4")