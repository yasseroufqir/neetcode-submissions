class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupe = defaultdict(list)
        for i in strs:
            count = [0]*26
            for char in i:
                count[ord(char)-ord('a')] +=1
            groupe[tuple(count)].append(i)
        return list(groupe.values())
            