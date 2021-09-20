# factorial of large numbers using preliminary digit-by-digit multiplication approach
# Day 6/100

N = int(input())
res = [1]
rem = 0
for i in range(2, N+1):
    for j in range(len(res)-1, -1, -1):
        temp = i*res[j]
        res[j] = temp%10 + rem
        rem = temp//10 + res[j]//10
        res[j] = res[j]%10
        if rem != 0 and j == 0:
            res.insert(0, rem)
            rem = 0
    

print("".join(res))