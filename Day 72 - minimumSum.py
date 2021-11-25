# Given an array of such that each element is from the range 0 to 9
# Find the minimum possible sum of two numbers formed using the elements of the array
# All digits in the given array must be used to form the two numbers
# Day 72/100


def solve(arr, n):

    if n == 1:
        return arr[0]
    arr.sort(reverse=True)

    n1 = [str(arr[i]) for i in range(0, n, 2) if arr[i] != 0]
    n2 = [str(arr[i]) for i in range(1, n, 2) if arr[i] != 0]

    n1 = int("".join(n1[::-1]))
    n2 = int("".join(n2[::-1]))

    return n1 + n2


#  Driver Code Starts
if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ans = solve(arr, n)
        print(ans)
        tc -= 1
