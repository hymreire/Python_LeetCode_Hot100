# 136. Single Number

from functools import reduce
from operator import xor
from typing import List

# 异或运算
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)

"""
异或（XOR）操作的含义：
- 异或是一个位运算操作符，用符号 ^ 表示
- 规则：相同为0，不同为1
  例如：0^0=0, 0^1=1, 1^0=1, 1^1=0

异或的重要性质：
1. a ^ a = 0          (任何数异或自己等于0)
2. a ^ 0 = a          (任何数异或0等于自己)
3. a ^ b = b ^ a      (交换律)
4. (a ^ b) ^ c = a ^ (b ^ c)  (结合律)

为什么这道题可以用异或解决？
题目要求：找出数组中只出现一次的数字（其他数字都出现两次）

思路：
- 如果我们将数组中所有数字进行异或操作
- 出现两次的数字会相互抵消（a ^ a = 0）
- 最后只剩下那个只出现一次的数字（0 ^ single = single）

示例：
nums = [2, 1, 2]
2 ^ 1 ^ 2 = (2 ^ 2) ^ 1 = 0 ^ 1 = 1

时间复杂度：O(n)
空间复杂度：O(1)
"""