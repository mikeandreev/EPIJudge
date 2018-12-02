from test_framework import generic_test

# Done

def buy_and_sell_stock_once_fwd(prices):
    profits = [0.0] * len(prices)
    profit = 0.0
    buy = float('inf')
    for i, p in enumerate(prices):
        if p > buy:
            if profit < p - buy: profit = p - buy
        else:
            if buy > p: buy = p
        profits[i] = profit
    return profits

def buy_and_sell_stock_twice(prices):
    if len(prices) == 0: return 0

    profit_fwd = buy_and_sell_stock_once_fwd(prices)

    total_profit = profit_fwd[-1]
    profit = 0.0
    sell = float('-inf')
    for i in reversed(range(1, len(prices))):
        p = prices[i]
        if p < sell:
            if profit < sell - p: profit = sell - p
        else:
            if sell < p: sell = p
        total_profit = max(total_profit, profit_fwd[i-1] + profit)

    return total_profit
## <<<

def buy_and_sell_stock_once_backwards(prices):
    profits = [0.0] * len(prices)
    profit = 0.0
    sell = float('-inf')
    for i in reversed(range(len(prices))):
        p = prices[i]
        if p < sell:
            if profit < sell - p: profit = sell - p
        else:
            if sell < p: sell = p
        profits[i] = profit
    return profits

def buy_and_sell_stock_twice1(prices):
    if len(prices) == 0: return 0

    profit_fwd = buy_and_sell_stock_once_fwd(prices)
    profit_bkwds = buy_and_sell_stock_once_backwards(prices)

    profit = 0.0
    for i in range(1, len(prices)):
        profit = max(profit, profit_fwd[i-1] + profit_bkwds[i])

    return max(profit, profit_fwd[-1])



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))

import unittest

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertEqual( buy_and_sell_stock_once_fwd([12,11,13,9,12,8,14,13,15]),
                                                      [ 0, 0, 2,2, 3,3, 6, 6, 7])
    def test2(self):
        self.assertEqual( buy_and_sell_stock_once_backwards([12,11,13,9,12,8,14,13,15]),
                                                            [ 7, 7, 7,7, 7,7, 2, 2, 0])
    def test3(self):
        self.assertEqual( buy_and_sell_stock_twice1([12,11,13,9,12,8,14,13,15]), 10.)
        self.assertEqual( buy_and_sell_stock_twice([12,11,13,9,12,8,14,13,15]), 10.)

