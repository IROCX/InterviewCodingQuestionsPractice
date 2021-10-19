# Find the largest rectangular area possible in a given histogram
# Day 35/100

from collections import deque


def getMaxArea(histogram):

    l = len(histogram)

    ls = 1
    stack = deque()
    stack.append(0)
    left = [-1] * l
    left[0] = 0
    max_area = -1

    if l == 1:
        return histogram[0]

    for i in range(1, l):
        if ls == 0:
            stack.append(i)
            left[i] = i
            ls += 1
        elif histogram[stack[-1]] > histogram[i]:
            while ls > 0 and histogram[stack[-1]] > histogram[i]:
                stack.pop()
                ls -= 1

            if ls == 0:
                left[i] = 0
            else:
                left[i] = stack[-1] + 1
            stack.append(i)
            ls += 1
        else:
            left[i] = stack[-1] + 1
            stack.append(i)
            ls += 1

    stack = [l - 1]
    ls = 1
    max_area = max(max_area, (l - 1 - left[-1] + 1) * histogram[-1])

    for i in range(l - 2, -1, -1):
        if ls == 0:
            stack.append(i)
            ls += 1
            max_area = max(max_area, (i - left[i] + 1) * histogram[i])
        elif histogram[stack[-1]] >= histogram[i]:
            while ls > 0 and histogram[stack[-1]] >= histogram[i]:
                stack.pop()
                ls -= 1
            if ls == 0:
                max_area = max(max_area, ((l - 1) - left[i] + 1) * histogram[i])
            else:
                max_area = max(max_area, ((stack[-1] - 1) - left[i] + 1) * histogram[i])
            stack.append(i)
            ls += 1
        else:
            max_area = max(max_area, (i - left[i] + 1) * histogram[i])
            stack.append(i)
            ls += 1

    return max_area


#  Driver Code Starts

if __name__ == "__main__":
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(getMaxArea(a))
