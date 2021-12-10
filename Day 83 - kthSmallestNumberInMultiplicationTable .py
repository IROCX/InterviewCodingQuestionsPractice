# Given three integers M, N and K. Consider a grid of M * N, where mat[i][j] = i * j (1 based index)
# Find the Kth smallest element in the M * N multiplication table
# Day 83/100


def findKthNumber(m, n, k):
    l = 1
    r = m * n

    while l < r:
        mid = (l + r) // 2
        if test(mid, m, n, k):
            r = mid
        else:
            l = mid + 1
    return l


def test(mid, m, n, k):
    count = 0
    for i in range(1, m + 1):
        add = min(mid // i, n)
        if add == 0:
            break
        else:
            count += add
    return count >= k


#  Driver Code Starts

t = int(input())
for _ in range(0, t):

    arr = list(map(int, input().split()))
    print(findKthNumber(arr[0], arr[1], arr[2]))
