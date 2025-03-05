# Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_len = 0
        max_str = ''
        # Check for odd length palindromes
        
        for mid in range( len(s) ):
            i , j = mid, mid
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > max_len:
                    max_str = s[i: j+1]
                    max_len = max( max_len, j - i + 1 )
                i-=1
                j+=1

            # Check for even length palindromes
            i, j = mid, mid + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > max_len:
                    max_str = s[i: j+1]
                    max_len = max( max_len, j - i + 1 )
                i-=1
                j+=1
            
        return max_str
