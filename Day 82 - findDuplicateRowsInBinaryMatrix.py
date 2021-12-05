# Given a binary matrix, find the duplicate rows
# Day 82/100


from collections import defaultdict


def defval():
    return 0


def repeatedRows(arr, m, n):

    mp = defaultdict(defval)

    for i in range(m):
        for j in range(n):
            arr[i][j] = str(arr[i][j])

    mp["".join(arr[0])] = 1
    res = []
    for i in range(1, m):
        temp = "".join(arr[i])

        if mp[temp] == 1:
            res.append(i)
        else:
            mp[temp] = 1

    return res


#  Driver Code Starts
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))

        arr = []
        for i in range(n):
            nums = list(map(int, input().strip().split()))
            arr.append(nums)

        ans = repeatedRows(arr, n, m)

        for x in ans:
            print(x, end=" ")

        print()
        tc -= 1
