class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for e in s:
            seen[e] = 1 + seen.get(e,0)
        for e in t:
            if e not in seen:
                return False
            else:
                seen[e]-= 1
        for e in seen.values():
            if e != 0:
                return False
        return True