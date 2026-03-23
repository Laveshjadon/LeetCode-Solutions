class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(1,len(prices)):
            # we have to take whenever graph go up just draw graph and than think of that 
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit 
       
        