class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count= 0
        for i in range(len(nums)):
            if nums[i] == 1:
                result+=1
                count = max(count,result)
            else:
                result = 0
        return count


    