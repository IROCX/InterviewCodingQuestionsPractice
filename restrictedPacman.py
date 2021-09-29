# given 2 number m, n - find the number of positive integers that can't be obtained by addition of these 2 numbers any number of times 
# Day 15/100

m, n = map(int, input().split())

# by Frobenius Coin Problem
# max number that can't be obtained by 2 given number
max_num = m*n - m - n

# by Chicken McNugget Theorem
# number of positive integers that can't be obtained by 2 given numbers 
res = (m-1)*(n-1)//2