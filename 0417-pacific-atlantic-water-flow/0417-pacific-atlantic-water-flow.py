class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        
        def bfs(starts):
            visited = set(starts)
            queue = list(starts)
            while queue:
                y, x = queue.pop(0)
                for dy, dx in [(0,1),(1,0),(-1,0),(0,-1)]:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny < m and 0 <= nx < n and (ny,nx) not in visited:
                        if heights[ny][nx] >= heights[y][x]:  # 역방향: 올라갈 수 있으면
                            visited.add((ny,nx))
                            queue.append((ny,nx))
            return visited
        
        pacific = [(i,0) for i in range(m)] + [(0,j) for j in range(n)]
        atlantic = [(i,n-1) for i in range(m)] + [(m-1,j) for j in range(n)]
        
        return list(bfs(pacific) & bfs(atlantic))