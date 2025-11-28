# 3258. Count Substrings That Satisfy K-Constraint I

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans=left=0
        cnt=[0,0] # 分别表示0、1的累计和
        for right,c in enumerate(s):
            cnt[ord(c)&1]+=1 # "0"的ASCII是48，"1"的ASCII是49，偶数二进制最后一位为0，奇数为1
            while cnt[0]>k and cnt[1]>k: # 不满足条件时才更新
                cnt[ord(s[left])&1]-=1
                left+=1
            ans+=right-left+1 # 实时更新
        return ans
# 时间复杂度：O(n)，n是s的长度
# 空间复杂度：O(1)