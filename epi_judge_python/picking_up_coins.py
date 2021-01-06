from test_framework import generic_test

#
# problem 16.9
#
# DONE
#

def maximum_revenue_v2(coins):
    n = len(coins)
    cache = [(0, coins[i]) for i in range(n)]

    for k in range(1, n):
        cache_next = [None] * (n-1)
        for i in range(n-k):
            j = i+k
            a = cache[i]
            b = cache[i+1]
            if k%2 == 1:
                if coins[i] + b[0] > coins[j] + a[0]:
                    cache_next[i] = (coins[i]+b[0], b[1])
                else:
                    cache_next[i] = (coins[j]+a[0], a[1])
            else:
                if coins[i] + b[1] > coins[j] + a[1]:
                    cache_next[i] = (b[0], coins[i] + b[1])
                else:
                    cache_next[i] = (a[0], coins[j] + a[1])
        cache = cache_next

    return cache[0][n%2]

def maximum_revenue_v1_1(coins):
    n = len(coins)
    cache = [[None] * n for _ in range(n)]

    for i in range(n):
        cache[i][i] = (0, coins[i])

    for k in range(1, n):
        for i in range(n-k):
            j = i+k
            a = cache[i][j-1]
            b = cache[i+1][j]
            if k%2 == 1:
                if coins[i] + b[0] > coins[j] + a[0]:
                    cache[i][j] = (coins[i]+b[0], b[1])
                else:
                    cache[i][j] = (coins[j]+a[0], a[1])
            else:
                if coins[i] + b[1] > coins[j] + a[1]:
                    cache[i][j] = (b[0], coins[i] + b[1])
                else:
                    cache[i][j] = (a[0], coins[j] + a[1])

    return cache[0][n-1][n%2]

def maximum_revenue_v1(coins):
    n = len(coins)
    cache = [[None] * (n+1) for _ in range(n)]

    for i in range(n):
        cache[i][i+1] = (0, coins[i])

    for k in range(2, n+1):
        for i in range(n-k+1):
            j = i+k
            a = cache[i][j-1]
            b = cache[i+1][j]
            if k%2 == 0:
                if coins[i] + b[0] > coins[j-1] + a[0]:
                    cache[i][j] = (coins[i]+b[0], b[1])
                else:
                    cache[i][j] = (coins[j-1]+a[0], a[1])
            else:
                if coins[i] + b[1] > coins[j-1] + a[1]:
                    cache[i][j] = (b[0], coins[i] + b[1])
                else:
                    cache[i][j] = (a[0], coins[j-1] + a[1])

    return cache[0][n][n%2]

def maximum_revenue(coins):
    return maximum_revenue_v2(coins)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
