# 1208. Get Equal Substrings Within Budget

# 滑动窗口，这题应该是子串（连续）转子串
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n=len(s)
        left=cost=maxlength=0
        for right in range(n):
            cost+=abs(ord(s[right])-ord(t[right])) # 字符转ASCII码
            while cost>maxCost:
                cost-=abs(ord(s[left])-ord(t[left]))
                left+=1
            maxlength=max(maxlength,right-left+1)
        return maxlength
# 时间复杂度O(n)、空间复杂度O(1)