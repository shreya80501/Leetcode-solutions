# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, max_index = 0, 0

        while i <= max_index:
            max_index = max( max_index, i + nums[i] )
            if max_index >= len( nums ) - 1:
                return True
            i = i + 1

        return False