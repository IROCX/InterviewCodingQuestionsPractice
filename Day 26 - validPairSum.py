# find the number of distinct pairs in the array having sum greater than 0
# Day 26/100


def ValidPair(arr, n):
    arr.sort()
    cost = 0
    i, j = 0, n - 1
    while i < j:
        if arr[i] + arr[j] > 0:
            cost += j - i
            j -= 1
        else:
            i += 1
    return cost


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ans = ValidPair(arr, n)
        print(ans)
