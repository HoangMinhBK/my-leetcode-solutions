class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten_oranges, is_any_fresh_oranges = self.findRottenOranges(grid)
        # If no orange is rotten and there are fresh oranges
        if not rotten_oranges and is_any_fresh_oranges:
            return -1

        res = 0

        # BFS Setup
        # Traversal queue
        queue = deque()
        # Track visited cells
        # key: row-col
        # Ex: grid[3][4] => key: "3-4"
        visited = set()

        for x, y in rotten_oranges:
            queue.append((x, y, 0))
            visited.add(str(x) + "-" + str(y))

        while queue:
            i, j, time_elapsed = queue.popleft()
            # Store elapsed time to res
            res = time_elapsed
            # Mark current orange is rotten
            grid[i][j] = 2
            # if top fresh
            if (
                i - 1 >= 0
                and grid[i - 1][j] == 1
                and str(i - 1) + "-" + str(j) not in visited
            ):
                queue.append((i - 1, j, time_elapsed + 1))
                visited.add(str(i - 1) + "-" + str(j))
            # if bottom fresh
            if (
                i + 1 < len(grid)
                and grid[i + 1][j] == 1
                and str(i + 1) + "-" + str(j) not in visited
            ):
                queue.append((i + 1, j, time_elapsed + 1))
                visited.add(str(i + 1) + "-" + str(j))
            # if left fresh
            if (
                j - 1 >= 0
                and grid[i][j - 1] == 1
                and str(i) + "-" + str(j - 1) not in visited
            ):
                queue.append((i, j - 1, time_elapsed + 1))
                visited.add(str(i) + "-" + str(j - 1))
            # if right fresh
            if (
                j + 1 < len(grid[0])
                and grid[i][j + 1] == 1
                and str(i) + "-" + str(j + 1) not in visited
            ):
                queue.append((i, j + 1, time_elapsed + 1))
                visited.add(str(i) + "-" + str(j + 1))

        if self.isRemainingFreshOranges(grid):
            return -1
        return res

    # Find all rotten oranges first, also check for any fresh oranges
    def findRottenOranges(self, grid):
        rottens = []
        is_any_fresh_oranges = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # if has any fresh oranges
                if grid[i][j] == 1:
                    is_any_fresh_oranges = True
                if grid[i][j] == 2:
                    rottens.append((i, j))

        return rottens, is_any_fresh_oranges

    def isRemainingFreshOranges(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return True
        return False

    # Time complexity: O(n*m), m,n <=10 => O(n)
    # Space complexity: O(n*m), m,n <=10 => O(n)
