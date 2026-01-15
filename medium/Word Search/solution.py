class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        chars, is_reversed = self.findStartingCharacters(board, word)
        if not chars:
            return False

        # Have to reverse the word if we search from the tail.
        if is_reversed:
            word = word[::-1]

        for x, y in chars:
            if self.dfs(x, y, 0, set(), board, word):
                return True
        return False

    def dfs(self, i, j, current_check_index, visited, board, word):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if (i, j) in visited:
            return False
        if board[i][j] != word[current_check_index]:
            return False
        if current_check_index == len(word) - 1:
            return True

        visited.add((i, j))

        # If any of the path search is found.
        found = (
            self.dfs(i + 1, j, current_check_index + 1, visited, board, word)
            or self.dfs(i - 1, j, current_check_index + 1, visited, board, word)
            or self.dfs(i, j + 1, current_check_index + 1, visited, board, word)
            or self.dfs(i, j - 1, current_check_index + 1, visited, board, word)
        )

        visited.remove((i, j))
        return found

    # Tip for optimization:
    # We consider the frequency of the first and last char of the word.
    # If one end is less frequent, then we start from that end.
    # For example: word = 'AAAAAAAAAAAB'
    # If we search from start, there are many possible ways to go, thus
    # time will increase. Therefore, go from the end in reversed, will be
    # much faster.
    def findStartingCharacters(self, board, word):
        first_char_locations = []
        last_char_locations = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    first_char_locations.append((i, j))
                if board[i][j] == word[-1]:
                    last_char_locations.append((i, j))

        if len(last_char_locations) < len(first_char_locations):
            return last_char_locations, True  # reversed is true
        return first_char_locations, False
