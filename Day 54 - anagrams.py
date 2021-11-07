# Given two strings, check whether two given strings are an anagram of each other or not
# Day 54/100

from collections import defaultdict

def defval():
    return 0


def isAnagram(self, a, b):
    d = defaultdict(defval)

    for i in a:
        d[i] += 1

    for i in b:
        if d[i] > 0:
            d[i] -= 1
        else:
            return False
    return True if sum(d.values()) == 0 else False


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = map(str, input().strip().split())
        if isAnagram(a, b):
            print("YES")
        else:
            print("NO")
