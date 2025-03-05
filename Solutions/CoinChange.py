# https://leetcode.com/problems/coin-change/description/

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
            
        dp = [-1]*( amount + 1 )

        for i in range( amount + 1 ):
            if i in coins:
                dp[i] = 1
            else:
                min_required = amount + 1
                for c in coins:
                    if i - c > 0 and dp[ i - c ] != -1:
                        min_required = min ( dp[ i - c ] + 1 , min_required )
                
                if min_required == amount + 1:
                    dp[i] = -1
                else:
                    dp[i] = min_required

        return dp[ amount ]
