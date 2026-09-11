class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L = []
        for i in range(len(nums)):
            if nums[i]!=val:
                L.append(nums[i])
        nums[:len(L)] = L
        return len(L)