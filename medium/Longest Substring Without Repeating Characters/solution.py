class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)

        # Base case
        if n <= 1:
            return n

        left, right = 0, 1
        current_set = {s[left]}
        while right < n:
            # Maintain a substring without repeating characters
            if s[right] not in current_set:
                current_set.add(s[right])
                right += 1
                res = max(res, len(current_set))
                continue

            # Ex: "a|abcd|bcd...."
            # If meet "b", then has the shrink the window until no duplicate left.
            # => "aab|cdb|cd..."
            if s[right] in current_set:
                while left < right:
                    if s[left] == s[right]:
                        left = self.move_left_pointer(current_set, s, left)
                        break
                    left = self.move_left_pointer(current_set, s, left)
        return res

    # Helper method to move left pointer:
    # Remove s[left] out of current_set
    # Move left pointer to the right
    def move_left_pointer(self, current_set, s, left):
        current_set.remove(s[left])
        left += 1
        return left
