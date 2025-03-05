# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len( nums ) == 1:
            return nums[0]
        if len( nums ) == 0:
            return 0

        max_sum = 0
        # If I rob index 0
        dp = [0] * ( len( nums ) )
        
        for i in range( len( nums ) ):
            dp[i] = max( dp[i-1] if i - 1 >= 0 else 0 , ( dp[i-2] if i-2 >= 0 else 0 ) + nums[i-1] )
        
        max_sum = max( max_sum , dp[-2] )

        # If I don't rob index 0
        dp = [0] * ( len( nums ) )
        
        for i in range( 1, len( nums ) ):
            dp[i] = max( dp[i-1] if i - 1 >= 0 else 0 , ( dp[i-2] if i-2 >= 0 else 0 ) + nums[i-1] )

        max_sum = max( max_sum , dp[-1] )

        return max_sum