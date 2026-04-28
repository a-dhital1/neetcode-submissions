class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        length = len(heights)

        maxi = 0

        pointer1 = 0
        pointer2 = length - 1

        while pointer1 < pointer2:

            area = min(heights[pointer1], heights[pointer2]) * (pointer2 - pointer1)

            if area > maxi:
                maxi = area

            if heights[pointer1] < heights[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1

        return maxi