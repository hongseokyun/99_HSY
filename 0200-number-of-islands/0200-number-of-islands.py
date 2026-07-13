class Solution(object):
    def numIslands(self, grid):
        n,m = len(grid),len(grid[0])
        visit = [[False for _ in range(m)] for _ in range(n)]
        dyx = [(1,0),(0,1),(-1,0),(0,-1)]
        cnt = 0
        arr = []

        def search(grid,visit) :
            if 0<=y<n and 0<=x<m :
                if (grid[y][x] == "1") and (visit[y][x] == False) :
                    return True
            return False

        for i in range(n) :
            for j in range(m) :
                y,x = i,j
                if search(grid,visit) :
                    arr.append((i,j))
                    visit[i][j] = True
                    cnt += 1
                while arr :
                    di,dj = arr.pop()
                    for dy,dx in dyx :
                        y,x = di+dy, dj+dx
                        if search(grid,visit) :
                            visit[y][x] = True
                            arr.append((y,x))
        return cnt