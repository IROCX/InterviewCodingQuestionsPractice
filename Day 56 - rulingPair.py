# Find maximum sum pair having sum of their digits equal
# Day 56/100


from collections import defaultdict

def defval():
    return []
    
    
def RulingPair(arr): 

    d = defaultdict(defval)
    for i in arr:
        temp = i
        sumx = 0
        while i > 0:
            sumx = sumx + i%10
            i = i // 10
        d[sumx].append(temp)
    
    ans = -1
    for i in d:
        if len(d[i])>1:
            d[i].sort(reverse=True)
            ans = max(ans, d[i][0] + d[i][1])
        
    return ans


#  Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(RulingPair(arr,n))
