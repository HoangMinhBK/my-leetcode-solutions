class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        # Last house and the first house are adjacent.
        # So that they cannot be robbed together.
        # So now there are 2 plans:
        # Plan A: Rob from house 0 to house n-2
        # Plan B: Rob from house 1 to house n-1
        # Compare 2 plans to see which one is better.

        # plan_A[i] is the best res so far at house i for plan A
        plan_A = [0] * (n - 1)
        plan_A[0] = nums[0]  # Must rob house 0 in plan A
        plan_A[1] = nums[0]  # Skip house 1
        for i in range(2, n - 1):
            plan_A[i] = max(plan_A[i - 2] + nums[i], plan_A[i - 1])

        # plan_B[i] is the best res so far at house i for plan B
        plan_B = [0] * n
        plan_B[0] = 0  # Skip house 0 in plan B
        plan_B[1] = nums[1]  # Must rob house 1 in plan B
        for i in range(2, n):
            plan_B[i] = max(plan_B[i - 2] + nums[i], plan_B[i - 1])
        return max(plan_A[n - 2], plan_B[n - 1])
