class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]  # slow = slow.next
            fast = nums[nums[fast]]  # fast = fast.next.next
            if slow == fast:
                break
        # Reset slow pointer to the start, now
        # fast and slow pointer moves at the the same
        # slow speed, when they meet, that is the start
        # of the cyclic linked list.

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# Time complexity: O(n)
# Space complexity: O(1)
