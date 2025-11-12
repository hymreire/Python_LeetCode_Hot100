# 46. Permutations

# 回溯=递归+撤销

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        path=[0]*n
        on_path=[False]*n
        def dfs(i): # 全局操作：填充第i个字符，然后递归
            if i==n: # 到底了，返回
                ans.append(path.copy())
                return
            for j in range(n): # 遍历数组，如果这个数还没有被选，选他
                if on_path[j]==False:
                    path[i]=nums[j]
                    on_path[j]=True
                    dfs(i+1)
                    on_path[j]=False # 撤销
        dfs(0)
        return ans