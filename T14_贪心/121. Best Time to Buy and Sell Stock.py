# 121. Best Time to Buy and Sell Stock

# 贪心算法：维护局部最值
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        ans=0
        for p in prices:
            ans=max(ans,p-minPrice)
            minPrice=min(minPrice,p)
        return ans