# W476_Q3

# 这题还可以使用数位DP做，后面有时间补充一下

# 照着灵神的解法写了一下答案
class Solution:
    def countDistinct(self, n: int) -> int:
        s=str(n)
        length_s=len(s)
        pow9=9**length_s
        ans=(pow9-9)//8 # 等比数列求和公式，错位相减法推导
        for i,x in enumerate(s):
            if x=='0':
                break # 某一位为0时，当前位只能取0，后面也没办法挑选了
            choice=int(x)-1 # 两种选择：一种不选最大值，则后面位数字自由，否则选最大值，递降，考虑下一位的选择
            if i==length_s-1:
                choice+=1 # 最后一位不会对后面的数字造成影响了，可以选择最大值
            pow9//=9 # 这意味着后面可以随便选，也就是9^(length_s-1-i)种选法
            ans+=pow9*choice # 这里的选法加上的是不选最大值的结果，选最大值的结果在while后面时计算
        return ans

# 灵神解答
# 数学：进制、排列组合
class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        m = len(s)

        # 计算长度小于 m 的不含 0 的整数个数
        # 9^1 + 9^2 + ... + 9^(m-1) = (9^m - 9) / 8（等比数列求和公式：错位相减法）
        pow9 = 9 ** m # 注意pow9是9的m次方
        ans = (pow9 - 9) // 8

        # 计算长度恰好等于 m 的不含 0 的整数个数
        for i, d in enumerate(s):
            if d == '0':  # 只能填 0，不合法，跳出循环
                break
            # 这一位填 1 到 d-1，后面的数位可以随便填 1 到 9
            v = int(d) - 1
            if i == m - 1:
                v += 1  # 最后一位可以等于 d
            pow9 //= 9
            ans += v * pow9
            # 然后，这一位填 d，继续遍历

        return ans