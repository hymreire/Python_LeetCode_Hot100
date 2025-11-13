# 55. Jump Game

# 贪心：如果当前最右可达索引不能到当前索引，直接False
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0 # 维护最右可以到达的索引
        for i, jump in enumerate(nums):
            if i > mx:  # 无法到达 i
                return False
            mx = max(mx, i + jump)  # 从 i 最右可以跳到 i+jump
        return True