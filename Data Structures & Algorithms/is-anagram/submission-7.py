class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Map = {}
        for letter in s:
            Map[letter] = Map.get(letter,0)+1
        for letter in t:
            Map[letter] = Map.get(letter,0)-1
        for e in Map.values():
            if e != 0:
                return False
        return True