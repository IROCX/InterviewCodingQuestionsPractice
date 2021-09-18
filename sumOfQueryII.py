# query based sum over given range for a given array - linear approach
# Day 4/100 

n = int(input())
arr = list(map(int, input().split()))
q = int(input())
queries = list(map(int, input().split()))

res = []
temp = arr

for i in range(1,n):
    arr[i]+=arr[i-1]

# print(arr)

for i in range(0,2*q,2):
    if queries[i] == 1:
        res.append(arr[queries[i+1]-1])
    else:
        res.append(arr[queries[i+1]-1]-arr[queries[i]-2])
        
print(res)