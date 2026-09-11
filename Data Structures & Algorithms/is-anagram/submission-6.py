class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Map = {}
        for e in s:
            Map[e] = 1+Map.get(e,0)
        for e in t:
            if e not in Map:
                return False
            else:
                Map[e]-=1
        for e in Map:
            if Map[e] != 0:
                return False
        return True