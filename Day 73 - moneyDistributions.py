# Find the number of ways in which N coins can be distributed among K pupils such that each pupil receives at least one coin each
# Day 73/100


from math import factorial


def totalWays(N, K):
    MOD = 1000000007

    if N < K:
        return 0

    den = factorial(k - 1) * factorial(n - k)

    res = factorial(N - 1) // den

    return res % MOD


#  Driver Code Starts
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, k = input().split()
        n = int(n)
        k = int(k)
        ans = totalWays(n, k)
        print(ans)
