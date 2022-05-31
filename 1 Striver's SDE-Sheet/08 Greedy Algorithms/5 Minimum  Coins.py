'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    where N is the size of DENOMINATIONS array/list.
    
    This Solution won't work for GFG minCOins check the wrong submission
    using binary search for detail
'''


denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]


def findMinimumCoins(amount):
    coinsCount = 0
    n = len(denominations)
    
    for i in range(n-1,-1,-1):
        while amount >= denominations[i]:
            num_coins = amount//denominations[i]
            coinsCount += num_coins
            amount = amount%denominations[i]
            
    return coinsCount