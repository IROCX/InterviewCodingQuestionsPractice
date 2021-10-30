import heapq


def kthSmallest(mat, n, k):
    # Your code goes here

    d = [[mat[0][i], i, 0] for i in range(n)]
    heapq.heapify(d)

    res = 0
    row = 1
    for i in range(k):
        temp = heapq.heappop(d)
        if temp[2]+1 < n:
            heapq.heappush(d, [mat[temp[2]+1][temp[1]], temp[1], temp[2]+1])

    return temp[0]


# Driver Code
def main():
    T = int(input())
    while(T > 0):
        n = int(input())
        mat = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]
        k = int(input())

        temp = 0
        for i in range(n):
            for j in range(n):
                mat[i][j] = line1[temp]
                temp += 1

        print(kthSmallest(mat, n, k))
        T -= 1


if __name__ == "__main__":
    main()
