class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            new_area = abs(j - i) * min(heights[i],heights[j])
            if new_area > area:
                area = new_area
                new_area = 1
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return area