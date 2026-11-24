class Solution(object):
    def maxProfit(self, prices):
        result = 0
        deff = 0
        min_element = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < min_element:
                min_element = prices[i]
            else:
                deff =prices[i] - min_element
                result = max(deff,result)
        return result

        