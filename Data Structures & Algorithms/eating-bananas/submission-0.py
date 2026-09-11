class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #naive approach is to try all the k from 1 to max(piles)
        l,r = 1 , max(piles)
        res = r
        while l<=r:
            m = (l+r)//2
            hours = 0
            for i in piles:
                hours+=math.ceil(i/m)
            if hours <= h:
                res = min(res , m)
                r = m-1
            else:
                l=m+1
        return res
        
            
