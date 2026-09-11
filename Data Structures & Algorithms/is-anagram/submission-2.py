class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # need to have the same length
            return False
        else:
            seen = {}
            for char in s:
                if char in seen: 
                    seen[char] += 1 #increment the value
                else:
                    seen[char] = 1 #initialize at one
            for char in t:
                if char not in seen:
                    return False
                seen[char] -= 1
                if seen[char] < 0:
                    return False # needs to be 0
            
            return True
                
                

