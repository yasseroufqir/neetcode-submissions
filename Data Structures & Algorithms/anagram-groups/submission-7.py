class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = defaultdict(list)
        #build a hash map for all the anagrams we already seen
        for e in strs:
            count = [0]*26
            for letter in e:
                count[ord(letter)-ord('a')]+=1
            seen[tuple(count)].append(e)

        return list(seen.values())