# find the smallest range that includes at least one element from each of the K sorted lists
# Day 18/100

from collections import defaultdict

def defval():
    return 0
from sys import maxsize

def smallestRange(arr, n, k):
    res = [(0, i) for i in arr[0]]
    for i in range(1, k):
        res.extend([(i, z) for z in arr[i]])
    res.sort(key=lambda x: x[1])

    d = defaultdict(defval)
    cost = maxsize
    ans = (-1, -1)
    i = 0
    j = 0
    total = 0
    while j < n*k:
                    
        d[res[j][0]]+=1
        if d[res[j][0]] == 1:
            total += 1
        
        if total == k:
            if res[j][1] - res[i][1] + 1 < cost:
                cost = res[j][1] - res[i][1] + 1
                ans = (res[i][1], res[j][1]) 
        
        if total == k:
            while total == k:
                if d[res[i][0]] > 1:
                    d[res[i][0]]-=1
                    i+=1
                else:
                    break
            if res[j][1] - res[i][1] + 1 < cost:
                cost = res[j][1] - res[i][1] +1
                ans = (res[i][1], res[j][1]) 
        
        j+=1    
        
    return ans

#  Driver Code Starts
t=int(input())
for _ in range(t):
    line=input().strip().split()
    n=int(line[0])
    k=int(line[1])
    numbers=[]
    for i in range(k):
        numbers.append([int(x) for x in input().strip().split()])
    r = smallestRange(numbers, n, k)
    print(r[0],r[1])
