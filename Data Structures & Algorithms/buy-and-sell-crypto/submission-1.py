class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        j = 0
        while j<len(prices)-1:
            buy = float("inf")
            sell = 0
            for b in range(j+1):
                if prices[b]<buy:
                    buy = prices[b]
            for s in range(j+1,len(prices)):
                if prices[s]>sell:
                    sell = prices[s]
            curprofit = sell - buy
            if curprofit>profit:
                profit=curprofit
            j+=1
        if profit <0:
            return 0
        return profit
