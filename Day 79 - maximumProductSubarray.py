# Given an array of integers (may be positive, negative or zero)
# Find the product of the maximum product subarray
# Day 79/100


def maxProduct(arr, n):
    mxx = mnn = arr[0]
    maxprod = arr[0]
    for i in range(1, n):
        mxx, mnn = max([arr[i], arr[i] * mxx, arr[i] * mnn]), min(
            [arr[i], arr[i] * mxx, arr[i] * mnn]
        )

        maxprod = max(maxprod, mxx)

    return maxprod


# Driver Code Starts
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ans = maxProduct(arr, n)
        print(ans)
        tc -= 1
