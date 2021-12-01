# Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2:
# 0 : Empty cell
# 1 : Cells have fresh oranges
# 2 : Cells have rotten oranges
# Determine what is the minimum time required to rot all oranges
# A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time

from collections import deque


class Solution:
    def isSafe(self, i, j, n, m):
        if i >= 0 and i < n and j >= 0 and j < m:
            return 1

        return 0

    def orangesRotting(self, grid):
        q = deque()
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        n = len(grid)
        if n == 0:
            return -1

        m = len(grid[0])
        fresh = 0

        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 2:
                    q.append([i, j])

                if grid[i][j] == 1:
                    fresh += 1

        timeTaken = 0
        while len(q) > 0:
            q_size = len(q)
            while q_size > 0:
                [x, y] = q[0]
                q.popleft()
                for k in range(0, 4):
                    if (
                        self.isSafe(x + dx[k], y + dy[k], n, m)
                        and grid[x + dx[k]][y + dy[k]] == 1
                    ):
                        grid[x + dx[k]][y + dy[k]] = 2
                        fresh -= 1
                        q.append([x + dx[k], y + dy[k]])

                q_size -= 1

            timeTaken += 1

        return -1 if fresh > 0 else timeTaken - 1


#  Driver Code Starts
from queue import Queue

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.orangesRotting(grid)
        print(ans)
