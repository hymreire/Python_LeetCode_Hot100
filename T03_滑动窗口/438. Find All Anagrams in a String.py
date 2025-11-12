# 438. Find All Anagrams in a String

from typing import List
from collections import Counter

# 方法1：定长滑窗
class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p=Counter(p) # 小字符串
        cnt_s=Counter()
        ans=[]
        for right,c in enumerate(s):
            cnt_s[c]+=1
            left=right-len(p)+1 # 考虑极端情况：窗口长度为1
            if left<0:
                continue # 等待初始窗口成型
            if cnt_p==cnt_s:
                ans.append(left)
            out=s[left] # 计算的是移除字符的名字
            cnt_s[out]-=1
            if cnt_s[out]==0:
                del cnt_s[out]
        return ans

# 方法2：
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        cnt_p=Counter(p)
        left=0
        for right,c in enumerate(s):
            cnt_p[c]-=1
            while cnt_p[c]<0: # while确保将所有多余字符移除
                cnt_p[s[left]]+=1 # s[left]确保将左指针右移
                left+=1
            if right-left+1==len(p):
                ans.append(left)
        return ans

if __name__ == "__main__":
    # 示例输入
    s = "cbaebabacd"
    p = "abc"

    # 运行测试用例
    solution = Solution()
    output = solution.findAnagrams(s, p)
    print("输出:", output)
    print("预期结果: [0, 6]")
    
    # s = "cbaebabacd"
    # p = "abc"
    # solution = Solution()
    # print(solution.findAnagrams(s, p))
    # # 预期结果
    # # [0, 6]