# n-th fibonacci number problem in n*log(n)
# matrix based approach with recursive power method
# M^n gives (n-1)th fibonacci number
# Day 24/100


class Solution:
    def TotalAnimal(self, N):
        # Code here
        self.fib = [1, 1]
        MOD = 1000000007
        a = b = 1

        l = len(self.fib)

        if l <= N:

            a = self.fib[-1]
            b = self.fib[-2]

            for i in range(l, N + 1):
                a, b = b, (a % MOD + b % MOD) % MOD
                self.fib.append(b)
        else:
            return self.fib[N]


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N = int(input())
        ob = Solution()
        ans = ob.TotalAnimal(N)
        print(ans)
