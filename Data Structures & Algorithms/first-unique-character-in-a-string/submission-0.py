class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        n = len(s)
        for i,c in enumerate(s):
            if c not in seen:
                seen[c] = i
            else:
                seen[c] = n
            
        res = n
        for c in seen:
            res = min(res,seen[c])

        return -1 if res == n else res
        