class Solution:
    def check(self, nums: List[int]) -> bool:
        #we use a sliding window
        length, n = 1,len(nums)
        if n == 1 : return True
        for i in range(1,2*n):
            if nums[(i-1)%n] <= nums[i%n]:
                length +=1
            else:
                length = 1
            if length == n:
                return True
        return False