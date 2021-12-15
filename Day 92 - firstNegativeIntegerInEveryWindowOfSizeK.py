# Given an array and a positive integer K
# Find the first negative integer for each and every window(contiguous subarray) of size K
# Day 92 / 100


def printFirstNegativeInteger(A, N, K):
    i = 0
    j = 0
    res = []
    while j < N and A[j] >= 0:
        j += 1

    while i <= N - K:
        if j < i:
            j += 1
            while j < N and A[j] >= 0:
                j += 1
        if j < i + K:
            res.append(A[j])
        else:
            res.append(0)

        i += 1
    return res


#  Driver Code Starts


def main():

    T = int(input())

    while T > 0:
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())

        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()
