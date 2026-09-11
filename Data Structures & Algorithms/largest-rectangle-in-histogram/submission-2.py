class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #it's a stack problem
        maxArea = 0
        stack =[] #index and height
        for i,h in enumerate(heights):
            start = i #because we should keep track of the width
            while stack and stack[-1][1]>h:
                index,height = stack.pop()
                maxArea = max(maxArea,height*(i - index))
                start = index #updating the start backwards
            stack.append((start,h))
        #we should not forget the elements that we extend till the end
        for i,h in stack:
            maxArea = max(maxArea,h*(len(heights)-i))
        
        return maxArea
            
