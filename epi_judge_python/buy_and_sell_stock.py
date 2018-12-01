from test_framework import generic_test

# DONE


def buy_and_sell_stock_once(prices):
    profit = 0.0
    buy = float('inf')
    for p in prices:
        if p > buy:
            if profit < p - buy: profit = p - buy
            #profit = max(profit, p - buy)
        else:
            if buy > p: buy = p
            #buy = min(buy, p)
    
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
