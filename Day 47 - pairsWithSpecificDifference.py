# Given an array, find max sum of disjoint pairs having difference strictly less than K
# Day 47/100


def maxSumPairWithDifferenceLessThanK(arr, N, K):
    arr.sort(reverse=True)
    i = 0
    j = 1

    if N <= 1:
        return 0
    res = 0
    while j < N:
        if abs(arr[j] - arr[i]) < K:
            res += arr[i]+arr[j]
            i = j+1
            j = j+2

        else:
            if j == i+1:
                j += 1
            i += 1

    return res

#  Driver Code Starts


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        K = int(input())
        print(maxSumPairWithDifferenceLessThanK(arr, N, K))

        T -= 1


if __name__ == "__main__":
    main()
