class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        r = 0
        hashSet = set()
        for i in range(len(nums)):
            if i-r > k :
                hashSet.remove(nums[r])
                r+=1
                
            if nums[i] in hashSet:
                return True
            hashSet.add(nums[i])
        return False