# Given two integer numbers, the base a and the index b, find the last digit of a^b
# Day 81/100


def getLastDigit(a, b):

    a = int(a)
    b = int(b)

    if b == 0:
        return 1

    temp = a % 10
    if temp in [0, 1, 5, 6]:
        return temp
    elif temp == 2:
        rems = [6, 2, 4, 8]
        return rems[b % 4]
    elif temp == 3:
        rems = [1, 3, 9, 7]
        return rems[b % 4]
    elif temp == 4:
        rems = [6, 4]
        return rems[b % 2]
    elif temp == 7:
        rems = [1, 7, 9, 3]
        return rems[b % 4]
    elif temp == 8:
        rems = [6, 8, 4, 2]
        return rems[b % 4]
    elif temp == 9:
        rems = [1, 9]
        return rems[b % 2]


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(str, input().split())

        print(getLastDigit(a, b))
