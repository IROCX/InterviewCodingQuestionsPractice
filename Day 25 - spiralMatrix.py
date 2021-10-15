# circular clockwise traversal of 2D matrix for n-th element
# Day 25/100


def findK(arr, n, m, k):
    ans = -1
    i = j = 0
    temp = 0
    preTemp = temp
    while temp < k:
        x = n - (i * 2)
        y = m - (j * 2)
        preTemp = temp
        if x == 1 and y == 1:
            temp += 1
        elif x == 1:
            temp += y
        elif y == 1:
            temp += x
        else:
            temp += x * 2 + (y - 2) * 2

        i += 1
        j += 1

    a, b = i - 1, j - 1
    i, j = a, b
    inc = 0
    flag2 = 0
    jinc = 1
    while True:

        while j < (m - b):
            preTemp += 1

            if preTemp == k:
                ans = arr[i][j]
                flag2 = 1
                break
            i += inc
            j += jinc
        if flag2:
            break
        if i == a and j == m - b:
            inc, jinc = jinc, inc
            j = j - 1
            i += 1

        while i < (n - a):
            preTemp += 1
            if preTemp == k:
                ans = arr[i][j]
                flag2 = 1
                break
            i += inc
            j += jinc
        if flag2:
            break
        if i == n - a and j == m - b - 1:
            inc, jinc = 0, -1
            i -= 1
            j -= 1

        while j >= (b):
            preTemp += 1
            if preTemp == k:
                ans = arr[i][j]
                flag2 = 1
                break
            i += inc
            j += jinc
        if flag2:
            break

        if j + 1 == b and i == n - a - 1:
            inc, jinc = -1, 0
            j += 1
            i -= 1

        while i >= a:
            preTemp += 1
            if preTemp == k:
                ans = arr[i][j]
                flag2 = 1
                break
            i += inc
            j += jinc
        if flag2:
            break

    return ans


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, m, k = map(int, input().split())
        mat = []
        for i in range(n):
            temp = list(map(int, input().split()))
            mat.append(temp)
        ans = findK(mat, n, m, k)
        print(ans)
