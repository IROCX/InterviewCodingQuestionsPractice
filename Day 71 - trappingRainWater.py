# Given an array non-negative integers representing the height of blocks
# If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season
# Day 71/100


def trappingWater(arr, n):

    res = 0

    l = [-1] * n
    l[0] = arr[0]
    r = [-1] * n
    r[-1] = arr[-1]

    for i in range(1, n):
        l[i] = max(l[i - 1], arr[i])
    for i in range(n - 2, -1, -1):
        r[i] = max(r[i + 1], arr[i])

    for i in range(n):
        res += min(l[i], r[i]) - arr[i]
    return res


#  Driver Code Starts
def main():
    T = int(input())
    while T > 0:

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        print(trappingWater(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
