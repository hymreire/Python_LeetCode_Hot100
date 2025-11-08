# 53. Maximum Subarray

# 方法一：前缀和+贪心（贪心就是每步计算局部最优，然后合并为全局最优）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=-inf
        pre_sum=min_pre_sum=0
        for x in nums:
            pre_sum+=x
            ans=max(pre_sum-min_pre_sum,ans) # 核心逻辑是j减i-1
            min_pre_sum=min(min_pre_sum,pre_sum) # 更新最小前缀和
        return ans

# 方法二：动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        f=[0]*n
        f[0]=nums[0]
        for i in range(1,n):
            f[i]=max(0,f[i-1])+nums[i]
        return max(f)

# 空间优化
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=-inf
        f0=0
        n=len(nums)
        for i in range(n):
            f0=max(f0,0)+nums[i]
            ans=max(ans,f0)
        return ans

# 方法三：分治【这不是官解和灵解，是Gemini根据官解实现的Python写法，可通过测试，但目前没时间看，先放在这里，以后有时间再分析】

# 2. 初始化变量 (定义 Status 数据结构)
class Status:
    def __init__(self, lSum, rSum, mSum, iSum):
        self.lSum = lSum
        self.rSum = rSum
        self.mSum = mSum
        self.iSum = iSum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # 3. 构建核心逻辑 (搭建递归框架)
        def get(l: int, r: int) -> Status:
            
            # 4a. 调整判断条件 (Base Case)
            if l == r:
                val = nums[l]
                return Status(val, val, val, val)
            
            # 3. (续) 核心逻辑
            m = (l + r) // 2
            l_status = get(l, m)
            r_status = get(m + 1, r)
            
            # 4b. 调用更新方法 (pushUp)
            return pushUp(l_status, r_status)

        # 4b. 调整更新方法 (实现 pushUp 合并逻辑)
        def pushUp(l: Status, r: Status) -> Status:
            iSum = l.iSum + r.iSum
            lSum = max(l.lSum, l.iSum + r.lSum)
            rSum = max(r.rSum, r.iSum + l.rSum)
            mSum = max(l.mSum, r.mSum, l.rSum + r.lSum)
            return Status(lSum, rSum, mSum, iSum)
        
        # 1. 确定最终输出 (主函数入口)
        return get(0, len(nums) - 1).mSum