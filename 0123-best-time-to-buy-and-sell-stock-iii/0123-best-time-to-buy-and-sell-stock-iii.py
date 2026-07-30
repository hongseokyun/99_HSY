class Solution(object):
    def maxProfit(self, prices):
        nums_len = len(prices)
        if nums_len == 1 :
            return 0
        if 1 < nums_len <= 3 :
            min_price = float('inf')
            max_profit = 0
            for price in prices:
                min_price = min(min_price, price)
                max_profit = max(max_profit, price - min_price)
            return max_profit
        
        dp1 = [0]*nums_len
        min_price = float('inf')
        max_profit = 0
        i = 0
        for i,price in enumerate(prices):
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            dp1[i] = max_profit

        dp2 = [0]*nums_len
        max_price = float('-inf')
        max_profit = 0
        i = 0
        for i,price in enumerate(prices[::-1]):
            max_price = max(max_price, price)
            max_profit = max(max_profit, max_price - price)
            dp2[i] = max_profit

        result = 0
        for k in range(nums_len):
            result = max(dp1[k]+dp2[nums_len-1-k],result)
        print(dp1)
        print(dp2)
        return result