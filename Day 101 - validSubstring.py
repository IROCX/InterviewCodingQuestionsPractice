# Given a string S consisting only of opening and closing parenthesis 'ie '('  and ')'
# Find the length of the longest valid(well-formed) parentheses substring
# Day 101 / 100


def findMaxLen(S):
    temp = [-1]
    res = 0
    for i in range(0, len(S)):
        if S[i] == "(":
            temp.append(i)
        else:
            temp.pop()
            if temp != []:
                res = max(res, i - temp[-1])
            else:
                temp.append(i)
    return res


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        S = input()

        print(findMaxLen(S))
