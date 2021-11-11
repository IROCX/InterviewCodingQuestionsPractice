# Given an array of integers and a range(L, R), find the number of subarrays having sum in the range L to R
# Day 58/100

def countSub(arr, n, x):

    st = 0
    end = 0
    sum = 0
    cnt = 0

    while end < n:

        sum += arr[end]

        while st <= end and sum > x:
            sum -= arr[st]
            st += 1

        cnt += end - st + 1
        end += 1

    return cnt


def countSubarray(n, a, L, R):

    Rcnt = countSub(a, n, R)

    Lcnt = countSub(a, n, L - 1)

    return Rcnt - Lcnt


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N, L, R = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        ans = countSubarray(N, A, L, R)
        print(ans)
