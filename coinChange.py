"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
"""

def coinChange(coins: List[int], amount: int) -> int:
    """Bruteforce"""
    coins.sort()
    
    def helper(amt):
        if amt == 0:
            return []
        if amt < coins[0]:
            return None
        max_ar = None
        for coin in coins:
            if amt - coin >= 0:
                r = helper(amt-coin)
                if r != None:
                    r = r[:]
                    r.append(coin)
                    
                    if max_ar == None or len(r) < len(max_ar):
                        max_ar = r
        return max_ar
    
    r = helper(amount)
    return -1 if r == None else len(r)

def coinChange(coins: List[int], amount: int) -> int:
    """Memoization"""
    coins.sort()
    
    def helper(amt, memo={}):
        if amt in memo:
            return memo[amt]
        if amt == 0:
            return []
        if amt < coins[0]:
            return None
        max_ar = None
        for coin in coins:
            if amt - coin >= 0:
                r = helper(amt-coin, memo)
                if r != None:
                    r = r[:]
                    r.append(coin)
                    
                    if max_ar == None or len(r) < len(max_ar):
                        max_ar = r
        memo[amt] = max_ar
        return max_ar
    
    r = helper(amount)
    return -1 if r == None else len(r)


def coinChange(coins: List[int], amount: int) -> int:
    """Tabulation"""
    coins.sort()
    
    dp = [math.inf for _ in range(amount+1)]
    dp[0] = 0
    
    for i in range(1, amount+1):
        for coin in coins:                
            if i-coin >= 0:                    
                dp[i] = min(dp[i-coin]+1, dp[i])
                
    
    return dp[amount] if dp[amount] < math.inf else -1



def coinChange(coins: List[int], amount: int) -> int:
    """
    Better (lookup)
    """
    count, prev = 0, 1 << amount
    
    while prev & 1 == 0:
        cur = prev
        for coin in coins:
            cur |= prev >> coin

        if prev == cur:
            return -1

        prev = cur
        count += 1

    return count