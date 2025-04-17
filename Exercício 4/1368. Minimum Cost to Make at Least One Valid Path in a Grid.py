class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        dq = deque()
        dq.append((0, 0, 0))
        visited = [[False] * n for _ in range(m)]

        while dq:
            i, j, cost = dq.popleft()

            if visited[i][j]:
                continue
            visited[i][j] = True

            if(i, j) == (m - 1, n - 1):
                return cost

            for k, (dx, dy) in enumerate(directions):
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[i][j] == k + 1:
                        dq.appendleft((ni, nj, cost))
                    else:
                        dq.append((ni, nj, cost + 1))

        return -1
