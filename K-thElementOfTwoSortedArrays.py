# K-th element of two sorted Arrays - linear approach
# Day 3/100 

n,m,k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

i=j=0
count = 0
res = -1
while i<n and j<m:
    count+=1
    if arr1[i]<=arr2[j]:
        
        if count == k:
            res = arr1[i]
            break
        i+=1
    else:
        if count == k:
            res = arr2[j]
            break
        j+=1

if count != k:
    while i < n:
        count+=1

        if count == k:
            res = arr1[i]
            break
        
        i+=1

if count != k:
    while j<m:
        count+=1
        
        if count == k:
            res = arr2[j]
            break

        j+=1

print(res)