# count number of triplets with sum smaller than x - 2 pointer approach extended
# Day 28/100


def countTriplets(arr, n, sumo):

    arr.sort()
    cost = 0

    for k in range(n):

        i, j = k + 1, n - 1
        while i <= j:
            if arr[k] + arr[i] + arr[j] >= sumo:
                j -= 1
            else:
                cost += j - i
                i += 1
    return cost


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        l = list(map(int, input().split()))
        n = l[0]
        k = l[1]
        a = list(map(int, input().split()))
        ans = countTriplets(a, n, k)
        print(ans)
