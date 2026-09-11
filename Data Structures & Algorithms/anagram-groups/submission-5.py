class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupes = defaultdict(list)
        for i in strs:
            count = [0]*26
            for char in i:
                count[ord(char)-ord('a')] += 1
            groupes[tuple(count)].append(i)
        return list(groupes.values())