class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        max_area = 0
        while left < right:
            # Record the max area during the discovery (try to compress right or left side)
            max_area = max(max_area, self.calculateArea(left, right, height))

            # Move the pointer at the shorter line inward.
            # Reason: the area is limited by the shorter line,
            # so moving the taller line won't help increase area. Moving shorter line can
            # help us find potentially bigger areas.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def calculateArea(self, left, right, height):
        return (right - left) * min(height[right], height[left])
