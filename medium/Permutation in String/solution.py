class Solution(object):
    def checkInclusion(self, s1, s2):
        n = len(s2)
        m = len(s1)

        # Base case:
        # If s1 is longer than s2, then false
        if m > n:
            return False

        left = 0

        # Find a valid starting position
        while left < n and s2[left] not in s1:
            left += 1

        # If we already scanned through the s2
        # but still cannot find any permutation of s1,
        # should return False immediately.
        if left >= n:
            return False

        right = left
        freq = Counter(s1)
        temp = defaultdict(int)

        while right < n:
            ch = s2[right]
            if ch not in freq:
                # reset window when invalid char found
                temp.clear()
                right += 1
                left = right
            else:
                temp[ch] += 1
                right += 1
                # If the frequency exceed the s1
                # shrink the window from the left until the
                # they are equal
                while temp[ch] > freq[ch]:
                    temp[s2[left]] -= 1
                    left += 1
                # Return true if a valid permutation found.
                if right - left == m:
                    return True

        return False


# Time complexity: O(n)
#   - 1 loop through s2
# Space complexity: O(n)
#   - 2 hashmaps of size m
