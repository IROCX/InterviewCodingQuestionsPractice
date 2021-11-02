# Given an integer array, find the maximum of the minimum of every window size in the array
# Day 49/100

def maxOfMin(arr, n):
    left = [-1]*n
    right = [n]*n

    stack = [(0, arr[0])]
    for i in range(1, n):

        if stack[-1][1] <= arr[i]:
            stack.append((i, arr[i]))
        else:
            while stack != [] and stack[-1][1] > arr[i]:
                temp = stack.pop()
                right[temp[0]] = i
            stack.append((i, arr[i]))

    while stack != []:
        temp = stack.pop()
        right[temp[0]] = n

    stack = [(n-1, arr[n-1])]
    for i in range(n-2, -1, -1):

        if stack == []:
            stack.append((i, arr[i]))
        elif stack[-1][1] <= arr[i]:
            stack.append((i, arr[i]))
        else:
            while stack != [] and stack[-1][1] > arr[i]:
                temp = stack.pop()
                left[temp[0]] = i
            stack.append((i, arr[i]))

    while stack != []:
        temp = stack.pop()
        left[temp[0]] = -1

    res = [0]*n
    for i in range(n):
        res[right[i]-left[i]-1-1] = max(res[right[i]-left[i]-1-1], arr[i])

    for i in range(n-2, -1, -1):
        res[i] = max(res[i], res[i+1])
    return res


#  Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        res = maxOfMin(a, n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
