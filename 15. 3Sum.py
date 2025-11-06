# 15. 3Sum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums=sorted(nums)
        for i in range(n-2): # n-3会把3个数字的数组直接跳掉，这里还是倾向于让j<k这个判断条件把n-1和n-2排掉
            if i>0 and nums[i]==nums[i-1]: # 相较于前而非相较于后，否则-1，-1，2就算不出来，会直接被跳掉！
                continue
            if nums[i]+nums[i+1]+nums[i+2]>0:
                break # 保序性，后面不会再有等于0的了
            if nums[i]+nums[-1]+nums[-2]<0:
                continue # 当前索引最大值也到不了0
            j,k=i+1,n-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s<0:
                    j+=1
                elif s>0:
                    k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    k-=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return ans

if __name__ == "__main__":
    # nums = [-1,0,1,2,-1,-4]
    nums = [0,0,0]
    solution = Solution()
    print(solution.threeSum(nums))