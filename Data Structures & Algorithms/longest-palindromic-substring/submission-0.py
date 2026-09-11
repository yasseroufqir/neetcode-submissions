class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        for i in range(len(s)):

            # odd length palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > (end - start):
                    start = l
                    end = r
                l -= 1
                r += 1

            # even length palindrome
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > (end - start):
                    start = l
                    end = r
                l -= 1
                r += 1

        return s[start:end + 1]

            
