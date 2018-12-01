from test_framework import generic_test

# WIP

def buy_and_sell_stock_twice(prices):
    profit = 0.0
    buy = float('inf')
    for p in prices:
        if p > buy:
            if profit < p - buy: profit = p - buy
        else:
            if buy > p: buy = p
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
