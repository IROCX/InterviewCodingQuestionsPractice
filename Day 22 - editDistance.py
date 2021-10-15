# minimum edit, add, delete operation to make s1 identical to s2
# dp approach
# Day 22/100


def editDistance(s, t):
    l1 = len(s)
    l2 = len(t)

    dp = [[0] * (l1 + 1) for i in range(l2 + 1)]

    for i in range(l1 + 1):
        dp[0][i] = i

    for i in range(l2 + 1):
        dp[i][0] = i

    for i in range(1, l2 + 1):
        for j in range(1, l1 + 1):
            #  print(i, j)
            mn = min([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]])

            if t[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = mn + 1
                #  d[s[j-1]] = 1

    res = dp[-1][-1]

    return res


#  Driver Code Starts

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s, t = input().split()

        ans = editDistance(s, t)
        print(ans)

