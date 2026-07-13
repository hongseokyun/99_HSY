class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        n, m = len(grid), len(grid[0])
        dyx = [(1,0),(0,1),(-1,0),(0,-1)]
        cnt = 0

        def ok(y, x):
            return 0 <= y < n and 0 <= x < m and grid[y][x] == "1"

        for i in range(n):
            for j in range(m):
                if ok(i, j):
                    cnt += 1
                    grid[i][j] = "0"          # 방문 표시를 grid 자체에
                    stack = [(i, j)]
                    while stack:
                        ci, cj = stack.pop()
                        for dy, dx in dyx:
                            ny, nx = ci + dy, cj + dx
                            if ok(ny, nx):
                                grid[ny][nx] = "0"
                                stack.append((ny, nx))
        return cnt