# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_set = set()
        max_len = 0
        j = 0
        for i in range( len(s) ):
            while i > j and s[i] in curr_set:
                curr_set.remove( s[j] )
                j = j + 1
            max_len = max( max_len, i - j + 1 )
            curr_set.add( s[i] )
        
        return max_len