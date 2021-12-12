# Given an array containing 0s and 1s
# Find the number of subarrays having equal number of 0s and 1s
# Day 89 / 100


from collections import defaultdict


def defval():
    return -1


def countSubarrWithEqualZeroAndOne(arr, n):

    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1

    mp = defaultdict(defval)

    mp[0] = 1
    curr = 0
    count = 0

    for i in range(n):
        curr += arr[i]

        if mp[curr] != -1:
            count += mp[curr]
            mp[curr] += 1
        else:
            mp[curr] = 1

    return count


#  Driver Code Starts
def main():
    T = int(input())
    while T > 0:

        n = int(input())
        arr = [int(x) for x in input().strip().split()]

        print(countSubarrWithEqualZeroAndOne(arr, n))

        T -= 1


if __name__ == "__main__":
    main()
