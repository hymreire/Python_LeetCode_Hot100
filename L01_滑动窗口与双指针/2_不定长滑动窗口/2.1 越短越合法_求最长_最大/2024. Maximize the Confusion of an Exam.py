# 2024. Maximize the Confusion of an Exam

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left=ans=0
        f0=f1=0
        for right,booler in enumerate(answerKey):
            if booler=='T':
                f1+=1
            else:
                f0+=1
            while f0>k and f1>k: # 假如f0>>k，在某个时刻f1>k，若left是f0，一次右移不能解决问题
                if answerKey[left]=='T':
                    f1-=1
                else:
                    f0-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans
# 时间复杂度O(n)、空间复杂度O(1)