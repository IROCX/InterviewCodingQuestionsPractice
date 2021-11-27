# You are given 2 numbers (n , m); the task is to find n√m (nth root of m).
# Day 74/100


from sys import maxsize


def NthRoot(n, m):

    x = 2
    acc = 0.01
    delx = maxsize
    while delx > acc:
        temp = ((n - 1) / n) * x + (m / (n * (x ** (n - 1))))
        delx = abs(x - temp)
        x = temp

    num = int(x)
    if pow(num, n) == m:
        return num
    else:
        return -1


#  Driver Code Starts
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        ans = NthRoot(n, m)
        print(ans)
