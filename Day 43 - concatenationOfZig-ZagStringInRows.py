# Given a string and number of rows ‘n’
# Print the string formed by concatenating n rows when the input string is written in row-wise Zig-Zag fashion
# Day 43/100


def convert(self, s, n):

    fence = [[] for i in range(n)]

    col = 0
    col_offset = 1

    if n == 1:
        return s
    else:
        for i in s:
            fence[col].append(i)
            col += col_offset
            # print(col, fence)
            if col == 0:
                col_offset = 1
            if col == n-1:
                col_offset = -1
        res = ""

    for i in range(n):
        res += "".join(fence[i])

    return res


#  Driver Code Starts
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()
        n = int(input())

        print(convert(Str, n))
