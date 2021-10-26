# Given an array A of N integers and an integer X.
# In one operation, you can change the ith element of the array to any integer value.
# Find minimum number of such operations required such that the bitwise AND of all the elements of the array is strictly greater than X.
# Day 42/100


class Solution:
    def count(self, N, A, X):
        # code here
        m1 = m2 = 0
        res = N
        for i in range(30, -1, -1):
            if (X >> i) & 1:
                m1 ^= 1 << i
                continue
            count = 0
            m2 = m1 ^ (1 << i)
            for j in A:
                if j & m2 == m2:
                    count += 1

            res = min(res, N-count)
        return res


#  Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, X = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(N, A, X)
        print(ans)
