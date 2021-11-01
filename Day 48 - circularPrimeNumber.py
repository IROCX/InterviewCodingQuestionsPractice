# Given a number N check if it is Circular Prime or Not.
# A prime number is a Circular Prime Number if all of its possible rotations are itself prime numbers.
# Day 48/100

def isCircularPrime(n):

    if n == 1:
        return 0

    digits = list(str(n))
    digits.sort(reverse=True)

    lgnum = int("".join(digits))

    sv = [True]*(lgnum+1)

    for i in range(2, lgnum+1):
        if sv[i] != False:
            for j in range(i**2, lgnum+1, i):
                sv[j] = False

    digits = list(str(n))
    for i in range(len(digits)):
        temp = int("".join(digits))
        if sv[temp] == False:
            return 0
        digits = digits[-1:] + digits[:-1:1]
    return 1


#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ans = isCircularPrime(n)
        print(ans)
