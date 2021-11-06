# Given two integers dividend and divisor, find the quotient of divide operation without using multiplication, division and mod operator.
# Day 53/100


def divide(dividend, divisor):

    if dividend == 0:
        return 0

    if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
        sign = 1
    else:
        sign = -1

    dividend, divisor = abs(dividend), abs(divisor)

    bits = len(bin(dividend)) - 2
    q = 0
    temp = 0
    for i in range(bits, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            q = q | 1 << i

    return q * sign


#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        inp = list(map(int, input().split()))

        a = inp[0]
        b = inp[1]

        ob = Solution()

        print(ob.divide(a, b))
