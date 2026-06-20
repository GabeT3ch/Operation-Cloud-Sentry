class Solution:
    def intit(self,prices):
        self.prices = prices


    def Maximum_profit(self,prices):
        min_price = prices[0] #start by assuming the first price is the cheapest
        max_profit = 0 # no profit yet we start at zero


        for price in prices:
            if price  < min_price: #this is saying if the price is less than the cheapest we have seen it becomes the new cheapest (BUY THE DIP)
                min_price = price
            else:
                profit = price - min_price   #otherwise the price is higher which means we need to calculate the profit if we sold today so simply put (todays price - or cheapest buy point) and if that profit beats our best so far it becomes the new best profit.
                if profit > max_profit:
                    max_profit = profit


        return max_profit




solution = Solution() #defining the solution class then passing in a test where the answer returned as 5 
print(solution.Maximum_profit([7,1,5,3,6,4])) 