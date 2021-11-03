# Given an array A of N integers find the maximum value of ∑arr[i]*i
# Day 50/100

class Solution:
    def Maximize(self, a, n):
        MOD = 1000000007
        a.sort()
        res = 0
        for i in range(n):
            res += (i*(a[i] % MOD)) % MOD
        return res % MOD


#  Driver Code Starts
for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.Maximize(arr, n))
