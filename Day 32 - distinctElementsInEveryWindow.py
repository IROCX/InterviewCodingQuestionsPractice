# Given an array and a number K, find the count of distinct elements in every window of size K in the array.
# Day 32/100

from collections import defaultdict


def defval():
    return 0


def countDistinct(A, N, K):
    res = []

    d = defaultdict(defval)
    count = 0

    i = 0
    j = 0
    while i < N - K + 1 and j <= N:
        if j < K:

            if d[A[j]] == 0:
                count += 1
            d[A[j]] += 1
            j += 1

        else:
            res.append(count)

            if j == N:
                break

            if d[A[j]] == 0:
                count += 1
            d[A[j]] += 1
            if d[A[i]] == 1:
                count -= 1
            d[A[i]] -= 1

            j += 1
            i += 1

    return res


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = countDistinct(arr, n, k)
        for i in res:
            print(i, end=" ")
        print()
