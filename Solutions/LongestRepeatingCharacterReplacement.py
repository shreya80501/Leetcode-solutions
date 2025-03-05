# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window_dict = {}
        j = 0
        max_len = 0

        for i in range( len(s) ):
            window_dict[s[i]] = window_dict[s[i]] + 1 if s[i] in window_dict else 1
            win_len = i - j + 1
            # Validate window
            if max( window_dict.values() ) + k < win_len:
                window_dict[s[j]] = window_dict[s[j]] - 1
                j = j + 1
            
            max_len = max( max_len , i - j + 1 )

        return max_len