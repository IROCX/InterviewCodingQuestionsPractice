# Given a A X B matrix with your initial position at the top-left cell.
# Find the number of possible unique paths to reach the bottom-right cell.
# Possible moves - down or right

# Day 44/100

def NumberOfPaths(self, a, b):

    dp = [[0]*a for i in range(b)]
    for i in range(a):
        dp[0][i] = 1
    for i in range(b):
        dp[i][0] = 1

    for i in range(1, b):
        for j in range(1, a):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]


#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a_b = [int(x) for x in input().strip().split()]
        a = a_b[0]
        b = a_b[1]
        print(NumberOfPaths(a, b))
