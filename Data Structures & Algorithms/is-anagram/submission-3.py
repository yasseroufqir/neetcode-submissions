class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            seen = {}
            for e in s:
                if e in seen:
                    seen[e]+=1
                else:
                    seen[e]=1
            for e in t:
                if e in seen:
                    seen[e]-=1
                else:
                    return False
            for e in seen.values():
                if e !=0:
                    return False
        return True
                
                

