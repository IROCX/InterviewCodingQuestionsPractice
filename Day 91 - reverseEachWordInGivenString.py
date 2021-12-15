# Given a String, reverse each word in it where the words are separated by dots
# Day 91 / 100


def reverseWords(s):
    s = s.split(".")
    res = []
    for i in s:
        res.append(i[::-1])

    res = ".".join(res)
    return res


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ans = reverseWords(s)
        print(ans)
