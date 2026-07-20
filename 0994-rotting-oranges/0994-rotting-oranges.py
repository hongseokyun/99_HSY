class Solution(object):
    def orangesRotting(self, grid):
        m,n = len(grid),len(grid[0])
        def visit(y,x,grid) :
            if 0 <= y <= m-1 and 0 <= x <= n-1 :
                if grid[y][x] != 0 :
                    return True
            return False

        arr = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    arr.append((i, j))
                    grid[i][j] = 0

        if not arr:
            # 신선한 오렌지가 남아있으면 -1
            for k in grid:
                for kk in k:
                    if kk == 1:
                        return -1
            return 0

        dyx = [(0,1),(1,0),(-1,0),(0,-1)]
        cnt = 0
        while arr :
            v_arr = arr[:]
            # print(arr)
            while v_arr :
                y,x = v_arr.pop(0)
                arr.pop(0)
                for dy,dx in dyx :
                    if visit(y+dy,x+dx,grid) :
                        arr.append((y+dy,x+dx))
                        grid[y+dy][x+dx] = 0
            cnt += 1
        for k in grid :
            for kk in k :
                if kk != 0:
                    return -1
        return cnt-1