# 300. Longest Increasing Subsequence

# 递归，记忆化搜索
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            res = 0 # 记录i左侧的最优结果
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1  # 加一提到循环外面 # dfs(j)右边还有一个i

        return max(dfs(i) for i in range(len(nums)))

# 递推
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = [0] * len(nums) # 以i结尾的最优值（右闭可选！）
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[:i]):
                if x > y:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        return max(f)

# 贪心+二分
# nums[i] = 长度为 i+1 的递增子序列的最小末尾元素（i<ng才有意义）
# 不同nums[i]值之间没有任何关系，nums[:ng]并非一个真实的递增子序列
# 这句话非常重要需要仔细思考
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ng = 0  # g 的长度 # [0,ng)维护一个有序数组
        for x in nums:
            j = bisect_left(nums, x, 0, ng) # [0,ng)查找第一个大等于x的索引
            nums[j] = x # 以x为末尾这一段数组去构建递增子序列
            if j == ng:  # 如果x能加入递增子序列的末尾，则ng再加长一格
                ng += 1
            # 这也就意味着如果x不能加入递增子序列的末尾，
            # 则以x为末尾这一段数组的递增长度必然不如之前的递增子序列
            # 若后续出现了大于末尾的数字，仍然可以从先前的递增子序列去构建更长递增子序列
        return ng