class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        s = list(s)
        while len(s) > 1:
            if s[-1] == "1":
                self.addOne(s)
            else:
                self.divideByTwo(s)
            count += 1

        if s[0] == "0":
            count += 1
        return count

    # Ex: 1101 -> 1110
    def addOne(self, s):
        s[-1] = "0"
        for i in range(len(s) - 2, -1, -1):
            if s[i] == "0":
                s[i] = "1"
                break
            else:
                s[i] = "0"
            # We don't need to insert '1' at the
            # start of the list.
            # Suppose we 111 -> 000 -> 00 -> 0 -> ''
            # Add 1 to count if s[0] == 0 achieve the same thing.

    # Ex: 1100 -> 110
    def divideByTwo(self, s):
        s.pop()
