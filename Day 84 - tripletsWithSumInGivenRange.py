# Given an array of N distinct integers and a range from L to R
# Count the number of triplets having a sum in the range [L, R]
# Day 84/100


def part(arr, n, x):
    res = 0
    for i in range(n):
        a = i + 1
        b = n - 1
        while a < b:
            sumx = arr[i] + arr[a] + arr[b]
            if sumx > x:
                b -= 1
            else:
                res += b - a
                a += 1

    return res


def countTriplets(arr, n, l, r):

    arr.sort()
    right = part(arr, n, r)
    left = part(arr, n, l - 1)

    return right - left


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        L, R = input().split()
        L = int(L)
        R = int(R)
        print(countTriplets(Arr, N, L, R))
