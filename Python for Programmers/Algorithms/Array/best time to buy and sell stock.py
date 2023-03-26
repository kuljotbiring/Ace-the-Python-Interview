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
    buy = 0
    sell = 1
    max_profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            curr_profit = prices[sell] - prices[buy]
            max_profit = max(max_profit, curr_profit)
        else:
            buy = sell
        sell += 1

    return max_profit
