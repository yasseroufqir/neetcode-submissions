class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i , h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index , height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start,h))
        
        n = len(heights)

        for index, height in stack:
            width = n - index
            maxArea = max(maxArea, height * width)

        return maxArea