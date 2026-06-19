class Solution:
    def intit(self,prices):
        self.prices = prices


    def Maximum_profit(self,prices):
        min_price = prices[0]
        max_profit = 0


        for price in prices:
            if price  < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit


        return max_profit




solution = Solution()
print(solution.Maximum_profit([7,1,5,3,6,4]))