# approach is using 2 pointer method

# arr = [1,2,3,7,5]
# sum = 12
# ans = [2,3,7] -> index [2,4]

arr = list(map(int, input().split()))
s = int(input())

maxlen = 0

l = len(arr)
sumx = 0
ans = [-1, -1]

i, j = 0, 0

while j<l:
    sumx = sum(arr[i:j+1])
    if sumx==s and maxlen<j-i+1:
        maxlen = j-i+1
        ans = [i, j]
    elif sumx>s:
        sumx-=arr[i]
        i+=1
    j+=1

if maxlen == 0:
    print(-1)
else:
    print(maxlen, ans)