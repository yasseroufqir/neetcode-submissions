class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Map = {}
        res = []
        for i , n in enumerate(nums2):
            Map[n] = i #we want the index
        for i in nums1:
            j = Map[i]
            answer = -1
            for k in range(j+1,len(nums2)):
                if nums2[k]> i:
                    answer = nums2[k]
                    break
            res.append(answer)
        return res