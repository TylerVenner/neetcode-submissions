class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j, areas = 0, len(heights) - 1, [0] * len(heights)
        max_area = 0
        while i < j:
            min_height = min(heights[i],heights[j])

            a = min_height * (j - i)

            if heights[i] == min_height:
                i += 1
            else:
                j -= 1

            if a > max_area:
                max_area = a
            

        return max_area
