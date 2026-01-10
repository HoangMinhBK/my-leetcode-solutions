class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i, j = 0, 0
        stack = []
        # We push into stack until we meet something to pop.
        # Then pop until invalid. Back to push mode.
        while i < len(pushed):
            stack.append(pushed[i])
            # When meet something to pop, pop until nothing to pop
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            i += 1

        # When we done pushing, try to pop the stack using remaining
        # pop sequence
        while j < len(popped):
            if popped[j] == stack[-1]:
                stack.pop()
                j += 1
            else:
                break
        # If the stack can be pop to empty, the sequence
        # is correct. Otherwise, not.
        return not stack


# Time complexity: O(n) (A stack used)
# Space complexity: O(len(pushed)+len(popped)) = O(n)
