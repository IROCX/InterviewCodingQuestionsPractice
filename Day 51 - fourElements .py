# Given an array A of N integers find whether a combination of four elements in the array whose sum is X exists or not.
# Day 51/100


def defval():
    return [-1, -1]


def find4Numbers(a, n, X):
    a.sort()

    for i in range(n):
        for j in range(i+1, n):
            rem = X - (a[i] + a[j])
            x = j+1
            y = n-1
            while x < y:
                if a[x] + a[y] == rem:
                    return 1
                elif a[x] + a[y] < rem:
                    x += 1
                else:
                    y -= 1
    return 0



#  Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        A = [int(x) for x in input().strip().split()]
        X = int(input())

        if find4Numbers(A, n, X):
            print(1)
        else:
            print(0)

        T -= 1


if __name__ == "__main__":
    main()
