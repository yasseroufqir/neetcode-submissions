class Solution:
    def longestPalindrome(self, s: str) -> str:
        #it either has a an even or an odd length
        res = ""
        resLen = 0
        #odd
        for i in range(len(s)):
            l , r = i , i
            while r < len(s) and l>=0 and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        #even
        for i in range(len(s)):
            l,r = i , i+1
            while r < len(s) and l>=0 and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return res    