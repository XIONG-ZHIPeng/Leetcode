class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy, sell = prices[0], prices[0]
        for i in range(1,len(prices)):
            if prices[i] > sell:
                sell = prices[i]
            else:
                profit += sell - buy
                buy, sell = prices[i], prices[i]
        else:
            profit += sell - buy
            
        return profit