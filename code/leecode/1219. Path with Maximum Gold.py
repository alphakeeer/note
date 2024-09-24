class Solution:
    def __init__(self) -> None:
        self.m = 0
        self.n = 0
        self.max_ans = 0

    def getMaximumGold(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.m = len(grid)-1
        self.n = len(grid[0])-1
        return self.rec_init(grid)

    # 对每个可行点(grid[i][j]!=0)进行探路
    def rec_init(self, grid: list[list[int]]):
        for i in range(self.m+1):
            for j in range(self.n+1):
                if grid[i][j] == 0:
                    continue
                num = grid[i][j]
                grid[i][j] = 0
                self.rec(grid, num, i, j)
                grid[i][j] = num
        return self.max_ans

    # 分别对四个方向进行探路，探路前设为0，探路后设回原数值并进行下一个方向
    def rec(self, grid: list[list[int]], num: int, x: int, y: int):
        if (y > 0 and grid[x][y-1] != 0):  # up
            cur_val = grid[x][y-1]
            grid[x][y-1] = 0
            self.rec(grid, num+cur_val, x, y-1)
            grid[x][y-1] = cur_val
        if (y < self.n and grid[x][y+1] != 0):  # down
            cur_val = grid[x][y+1]
            grid[x][y+1] = 0
            self.rec(grid, num+cur_val, x, y+1)
            grid[x][y+1] = cur_val
        if (x > 0 and grid[x-1][y] != 0):  # left
            cur_val = grid[x-1][y]
            grid[x-1][y] = 0
            self.rec(grid, num+cur_val, x-1, y)
            grid[x-1][y] = cur_val
        if (x < self.m and grid[x+1][y] != 0):  # right
            cur_val = grid[x+1][y]
            grid[x+1][y] = 0
            self.rec(grid, num+cur_val, x+1, y)
            grid[x+1][y] = cur_val
        if num > self.max_ans:
            self.max_ans = num


s = Solution()
grid = [[0, 6, 0],
        [5, 8, 7],
        [0, 9, 0]]
grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]

print(s.getMaximumGold(grid))


class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(x: int, y: int, gold: int) -> None:
            gold += grid[x][y]
            nonlocal ans
            ans = max(ans, gold)

            rec = grid[x][y]
            grid[x][y] = 0

            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                    dfs(nx, ny, gold)

            grid[x][y] = rec

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    dfs(i, j, 0)

        return ans
