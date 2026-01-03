class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        # base case:
        if n == 1:
            return [0]

        res = [0] * n

        # Maintain a monotonic decreasing stack (get smaller when go to the top stack)
        # The stack is to store the index for tempatures comparison
        monotonic_stack = []
        # Comparing the current day with the top of the stack
        for i in range(n - 1, -1, -1):
            # if the top of stack is colder than the current day, we have to pop the top
            # until we find a warmer day than current day.
            while (
                monotonic_stack and temperatures[i] >= temperatures[monotonic_stack[-1]]
            ):
                monotonic_stack.pop()
            # After that, the top will automatically the warmer day than today.
            if monotonic_stack:
                # Store the res
                res[i] = monotonic_stack[-1] - i
            # Add the current day into the stack for future comparison
            monotonic_stack.append(i)
        return res

        # Time complexity: O(n) (One for loop through the input list)
        # Space complexity: O(n) (Use an additional stack)
