# 1456. Maximum Number of Vowels in a Substring of Given Length

# 自己写的答案，优化部分没想到，按照灵神的解法补了一下
Vowel='a','e','i','o','u'
def mapping(letter):
    if letter in Vowel:
        return 1
    else:
        return 0
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # 思路，从左到右遍历字符串，如果字符串右索引超过k-1，则将左索引向右
        ans=tmp=0
        left=0
        n=len(s)
        for right,letter in enumerate(s):
            tmp+=mapping(letter)
            if right-left==k:
                tmp-=mapping(s[left])
                left+=1
            ans=max(ans,tmp)
            if ans==k: # 优化，ans最大为k
                break
        return ans

# 灵神的代码，整体优于我的代码
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = vowel = 0
        for i, c in enumerate(s):  # 枚举窗口右端点 i
            # 1. 右端点进入窗口
            if c in "aeiou":
                vowel += 1

            left = i - k + 1  # 窗口左端点
            if left < 0:  # 窗口大小不足 k，尚未形成第一个窗口
                continue

            # 2. 更新答案
            ans = max(ans, vowel)
            if ans == k:  # 答案已经等于理论最大值
                break  # 无需再循环

            # 3. 左端点离开窗口，为下一个循环做准备
            if s[left] in "aeiou":
                vowel -= 1
        return ans