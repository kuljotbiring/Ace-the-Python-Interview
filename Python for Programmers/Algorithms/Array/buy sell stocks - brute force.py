"""
Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made from
buying on one day and selling on another.

In an array of prices, each index represents a day, and the value on that index represents the price of the stocks on
that day.

Here is the way to calculate the profit:

    Profit = Selling Price - Buying Price

Note that you need to buy the stocks before you sell them so the day (index) indicating the buying price should be
before the day (index) indicating the selling price.
"""


def buy_and_sell_stock_once(prices):
    max_profit = 0

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i]:
                max_profit = prices[j] - prices[i]
    return max_profit


stocks = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

print(buy_and_sell_stock_once(stocks))
