# longest subarray with sum equal to zero
# Day 11/100 

from collections import defaultdict

def def_value():
    return -5

arr = list(map(int, input().split()))
n = len(arr)

sumx = 0
maxlen = 0

mp = defaultdict(def_value)
mp[0] = -1

for i in range(n):
    sumx += arr[i]
    if mp[sumx] != -5:
        maxlen = max(maxlen, i-mp[sumx])
    else:
        mp[sumx] = i

print(maxlen)