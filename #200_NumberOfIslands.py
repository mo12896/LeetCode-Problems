# 200. Number of Islands (Medium)
# https://leetcode.com/problems/number-of-islands/
# https://www.youtube.com/watch?v=U6-X_QOwPcs&list=PLU_sdQYzUj2keVENTP0a5rdykRSgg9Wp-

class Solution:
    def numIslands(self, grid):

        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    counter += 1
                    # recursively call depth first search
                    self.call_dfs(grid, i, j)
        return counter

    def call_dfs(self, grid, i, j):
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1 or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        self.call_dfs(grid, i - 1, j)  # up
        self.call_dfs(grid, i + 1, j)  # down
        self.call_dfs(grid, i, j - 1)  # left
        self.call_dfs(grid, i, j + 1)  # right


if __name__ == "__main__":
    solution = Solution()
    # testcase 1
    #input = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    # testcase 2
    input = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    output = solution.numIslands(input)
    print(output)