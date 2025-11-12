# 78. Subsets

# 选与不选
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        path=[]
        def dfs(i):
            if i==n:
                ans.append(path.copy())
                return
            dfs(i+1) # 不选
            path.append(nums[i])
            dfs(i+1) # 选
            path.pop() # 撤销
        dfs(0)
        return ans

# 枚举
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path=[]
        n=len(nums)
        ans=[]
        def dfs(i): # 枚举子集
            ans.append(path.copy())
            for j in range(i,n): # 循环条件
                path.append(nums[j])
                dfs(j+1) # 枚举
                path.pop()
        dfs(0)
        return ans

# 二进制枚举
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        for i in range(1<<n): # 左移的二进制形式，刚好代表了子集中选与不选的2^n中情况
            # &1将高位的1全部置0，只判断i的第j位是否为1，
            # 用这种办法正好能将i的二进制形式转换为对应的数值
            subset=[x for j,x in enumerate(nums) if i>>j&1]
            ans.append(subset)
        return ans