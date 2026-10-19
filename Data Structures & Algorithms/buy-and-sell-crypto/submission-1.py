class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1

        maxprofit = 0
        while r < len(prices):
            curr = prices[r] - prices[l]
            if curr > maxprofit:
                maxprofit = curr
            
            if prices[l] > prices[r]:
                l = r
            r += 1
        return maxprofit
