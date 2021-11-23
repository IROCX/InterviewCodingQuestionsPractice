# Given an array of N integers, find the minimum number of jumps to reach the end of the array (starting from the first element)
# Day 69/100


def minJumps(arr, n):
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1

    rc = arr[0]
    step = arr[0]
    st = 1
    for i in range(1, n):
        if i > rc:
            break

        rc = max(rc, i + arr[i])
        step -= 1

        if i != n - 1 and step == 0:
            st += 1
            step = rc - i
    if rc >= n:
        return st
    else:
        return -1


#  Driver Code Starts
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        Arr = [int(x) for x in input().split()]

        ans = minJumps(Arr, n)
        print(ans)
