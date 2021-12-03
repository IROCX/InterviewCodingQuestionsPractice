# Given an array of positive integers
# Find the minimum number of swaps required to bring all the numbers less than or equal to k together
# Day 80/100


def minSwap(arr, n, k):

    count = 0
    for i in range(n):
        if arr[i] <= k:
            count += 1

    count2 = 0
    for i in range(count):
        if arr[i] <= k:
            count2 += 1

    res = count - count2

    i = 1
    while i + count <= n:
        if arr[i - 1] <= k:
            count2 -= 1
        if arr[i + count - 1] <= k:
            count2 += 1
        res = min(res, count - count2)
        i += 1
    return res


#  Driver Code Starts
for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
