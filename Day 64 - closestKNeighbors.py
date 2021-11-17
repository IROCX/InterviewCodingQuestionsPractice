# Given a postion X, number of houses N, an integer K and distance between each neighbor house
# Find the closest k neighbors based on distance from X (absolute difference between numbers given in array)
# Day 64/100

import heapq

def Kclosest(arr, n, x, k):

    temp = arr.copy()
    for i in range(n):
        temp[i] = (abs(temp[i]-x), temp[i], i)

    heapq.heapify(temp)

    res = [None]*k
    j = 0

    for i in range(k):
        ind = heapq.heappop(temp)
        res[j] = arr[ind[2]]
        j+=1
        
    res.sort()
    
    return res


#Driver Code Starts.
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int( line[0] )
        x=int( line[1] )
        k=int( line[2] )
        arr=[int(x) for x in input().strip().split()]

        result=Kclosest(arr, n, x, k)
        for i in result:
            print(i, end=' ')
        print()