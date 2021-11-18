# Given N activities with their start and finish day given in array start[ ] and end[ ]
# Find maximum number of activities that can be performed by a single person, on at a time
# Day 65/100


def getCompatibleInterval(timings, i, start):

    st = 0
    en = i - 1
    mn = -1
    while st <= en:
        mid = (st + en) // 2
        if timings[mid][1] >= start:
            en = mid - 1
        else:
            mn = mid
            st = mid + 1

    return mn


def activitySelection(n, start, end):

    timings = list(zip(start, end))
    timings.sort(key=lambda x: x[1])

    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        ind = getCompatibleInterval(timings, i, timings[i][0])
        dp[i] = max(dp[i - 1], dp[ind] + 1)

    return dp[-1]


#  Driver Code Starts
if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        print(activitySelection(n, start, end))
