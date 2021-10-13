# find if C can be formed by interleaving A & B
# DP approach
# Day 29/100


def isInterleave(A, B, C):
    l1, l2 = len(A), len(B)
    dp = [[None] * (l2 + 1) for i in range(l1 + 1)]

    if l1 + l2 != len(C):
        return 0

    dp[0][0] = True

    for i in range(1, l2 + 1):
        if C[i - 1] == B[i - 1]:
            dp[0][i] = dp[0][i - 1]
        else:
            dp[0][i] = False

    for i in range(1, l1 + 1):
        if C[i - 1] == A[i - 1]:
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = False

    for i in range(1, l1 + 1):  # A
        for j in range(1, l2 + 1):  # B
            t1, t2 = None, None
            if C[i + j - 1] == A[i - 1]:
                t1 = dp[i - 1][j]
            else:
                t1 = False
            if C[i + j - 1] == B[j - 1]:
                t2 = dp[i][j - 1]
            else:
                t2 = False
            dp[i][j] = t1 or t2
    return 1 if dp[-1][-1] == True else 0


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        if isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)
