# get all unique permutations of given array - array may contain duplicate elements
# Day 31/100


from collections import Counter


def dfs(perm, arr, d, res):
    if len(perm) == len(arr):
        res.append(perm.copy())
        return

    for i in d:
        if d[i] > 0:
            perm.append(i)
            d[i] -= 1

            dfs(perm, arr, d, res)

            d[i] += 1
            perm.pop()


def uniquePerms(arr, n):
    res = []
    perm = []
    d = Counter(arr)

    dfs(perm, arr, d, res)

    return res


#  Driver Code Starts

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        res = uniquePerms(arr, n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j], end=" ")
            print()
