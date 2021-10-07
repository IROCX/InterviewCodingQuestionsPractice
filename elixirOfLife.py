# given a string, find max frequency of a substring which is prefix, suffix and occurs maximum time in the string
# Day 23/100


def maxFrequency(s):
    i = 0
    l = len(s)

    while i < l:
        if s[: i + 1] == s[-(i + 1) :]:
            break
        else:
            i += 1

    if i == l - 1:
        return 1
    else:
        return s.count(s[: i + 1])


if __name__ == "__main__":

    s = input()

    res = maxFrequency(s)
    print(res)
