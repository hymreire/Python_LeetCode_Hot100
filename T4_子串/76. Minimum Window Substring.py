# 76. Minimum Window Substring

# 滑动窗口
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cs=Counter()
        ct=Counter(t)
        n=len(s)
        ans_left,ans_right=-1,n
        left=0
        for right,x in enumerate(s):
            cs[x]+=1 # 先入  # 哈希表输入字符输出索引
            while ct<=cs:
                if right-left<ans_right-ans_left:
                    ans_left,ans_right=left,right
                cs[s[left]]-=1 # 哈希表输入字符输出索引
                left+=1 # 再出
        return "" if ans_left<0 else s[ans_left:ans_right+1]

# 优化：感觉就是加了一个表示种类差异的less来做剪枝
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt=defaultdict(int)
        for c in t:
            cnt[c]+=1 # 记录下t的字符数量
        less=len(cnt) # 记录下t的字符种类
        n=len(s)
        ans_left=-1
        ans_right=n
        left=0
        for right,c in enumerate(s): # 遍历字符串
            cnt[c]-=1 # 先入
            if cnt[c]==0:
                less-=1 # 种类差异减小
            while less==0: # 没有种类差异时
                # 更新最小覆盖子串
                if right-left<ans_right-ans_left:
                    ans_left,ans_right=left,right
                cnt[s[left]]+=1
                if cnt[s[left]]>0:
                    less+=1
                left+=1
        return "" if ans_left<0 else s[ans_left:ans_right+1]