class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        if numbers[start] >= 0:
            end = self.findEndWhenAllPostiveOrStartWhenAllNegative(
                numbers, target, False
            )
        if numbers[end] <= 0:
            start = self.findEndWhenAllPostiveOrStartWhenAllNegative(
                numbers, target, True
            )

        while start < end:
            if numbers[start] + numbers[end] == target:
                return start + 1, end + 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1

    # This is to improve runtime in case all negative and all positive. The point was to
    # cut down the array by half when finding 2 numbers adding up to the target.
    def findEndWhenAllPostiveOrStartWhenAllNegative(self, numbers, target, negative):
        point = 0
        if not negative:
            for i in range(len(numbers)):
                if numbers[i] > target:
                    return point
                point = i
        else:
            for i in range(len(numbers) - 1, -1, -1):
                if numbers[i] < target:
                    return point
                point = i
        return point
