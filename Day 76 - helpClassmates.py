# Given array of integers, find the next strictly smaller element for each element.
# Day 76/100


def help_classmate(arr, n):

    stack = []
    res = [-1] * n

    for i in range(n):
        if stack == []:
            stack.append((i, arr[i]))
        else:
            if stack[-1][1] > arr[i]:
                while stack != [] and stack[-1][1] > arr[i]:
                    temp = stack.pop()
                    res[temp[0]] = arr[i]
            stack.append((i, arr[i]))
    return res


#  Driver Code Starts
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]

        result = help_classmate(arr, n)
        for i in result:
            print(i, end=" ")
        print()
