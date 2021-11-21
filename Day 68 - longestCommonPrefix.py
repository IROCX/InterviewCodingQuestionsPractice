# Given two strings str1 and str2 of the same length, find the longest prefix of str1 which is common in str2
# Day 68/100


def longestCommonPrefix(str1, str2):

    i = 0
    j = 0
    diff = -1
    maxans = [-1, -1]
    ans = [-1, -1]
    flag = 1
    l = len(str2)
    while j < l:
        if (str1[i] == str2[j]) and flag:
            ans[0] = 0
            ans[1] = 0
            if diff < (ans[1] - ans[0]):
                maxans = ans.copy()
                diff = ans[1] - ans[0]
            flag = 0
            i += 1
            j += 1
        elif str1[i] == str2[j]:
            ans[1] = i
            if diff < (ans[1] - ans[0]):
                maxans = ans.copy()
                diff = ans[1] - ans[0]

            i += 1
            j += 1
        else:
            i = 0
            if flag:
                j += 1
            flag = 1

    return maxans


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        str1 = input()
        str2 = input()
        ans = longestCommonPrefix(str1, str2)
        if ans[0] == -1:
            print(-1)
        else:
            print(ans[0], ans[1])
