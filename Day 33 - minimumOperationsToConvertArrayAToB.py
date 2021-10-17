# Given two Arrays A[] and B[] of length N and M respectively.
# Find the minimum number of insertions and deletions on the array A[], required to make both the arrays identical.
# Note: Array B[] is sorted and all its elements are distinct.
# Day 33/100

from collections import Counter


def bs(arr, k):

    l = 0
    r = len(arr) - 1
    ans = -1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] < k:

            l = mid + 1
        else:
            ans = mid
            r = mid - 1
    return ans


def minInsAndDel(A, B, N, M):

    d = Counter(B)
    temp = []

    for i in range(N):
        if d[A[i]]:
            temp.append(A[i])

    res = []

    for i in temp:
        ind = bs(res, i)
        if ind == -1:
            res.append(i)
        else:
            res[ind] = i

    return M + N - 2 * len(res)


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        print(minInsAndDel(A, B, N, M))
# } Driver Code Ends
