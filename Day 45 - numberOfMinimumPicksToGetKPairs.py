# Given number of socks for each color in array.
# Find minimum number of socks needed to be picked to get k pairs gauranteed.

# Day 45/100

def find_min(a, n, k):
    total_pairs = 0
    for i in a:
        total_pairs += i//2

    if total_pairs < k:
        return -1
    else:
        sumx = 0
        for i in a:
            if i & 1:
                sumx += i//2
            else:
                sumx += (i//2)-1

        if sumx >= k:
            return 2*(k-1) + n + 1
        else:
            return sumx*2 + n + k-sumx


#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        k = int(input())
        print(find_min(a, n, k))
