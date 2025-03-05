# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * ( target + 1 )

        for i in range( target + 1 ):
            num_ways = 0
            for c in nums:
                num_ways = num_ways + 1 if c == i else num_ways
                num_ways = num_ways + ( dp[i - c] if i - c >= 0 else 0 )
            
            dp[i] = num_ways

        return dp[target]