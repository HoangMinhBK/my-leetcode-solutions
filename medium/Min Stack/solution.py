class MinStack(object):

    def __init__(self):
        # Main stack is for O(1) pop, push, top
        # Mono stack is for O(1) getMin
        # Mono stack maintains a non-increasing order from bottom to top.
        # By doing this, the top of mono_stack will be min and can be
        # extracted in O(1) time.
        self.main_stack = []
        self.mono_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.main_stack.append(val)
        # if mono_stack is empty or top of mono_stack >= curren val
        # Update the mono_stack, still remaining the non-increasing order
        if not self.mono_stack or self.mono_stack[-1] >= val:
            self.mono_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if not self.main_stack:
            return
        val = self.main_stack.pop()
        # Have to update the mono_stack as well
        if self.mono_stack and val == self.mono_stack[-1]:
            self.mono_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.main_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mono_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
