# maximum difference (number of 0s – number of 1s) of zeros and ones in binary string - n the case of all 1s, the answer will be -1
# Day 20/100

from sys import maxsize

S = input()

l = len(S)
sum1 = 0
sum0 = 0
max_diff = -1 * (maxsize - 1)
curr_diff = 0

if S.count('1') == l:
    max_diff = -1
elif S.count('0') == l:
    max_diff = l
else:
    for i in range(l):
        if S[i] == '1':
            sum1+=1
            if sum0-sum1 > -1:
                curr_diff = sum0-sum1
            else:
                sum1=1
                sum0=0
                curr_diff = -1
        else:
            sum0+=1
            if sum0-sum1 > 1:
                curr_diff = sum0-sum1
            else:
                sum1=0
                sum0=1
                curr_diff = 1
            
        max_diff = max(curr_diff, max_diff)
print(max_diff)
