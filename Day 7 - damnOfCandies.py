# maximization problem
# Day 7/100

n = int(input())
height = list(map(int, input().split()))

i , j = 0, n-1
        
max_area = 0

while i < j:
    temp = min(height[i], height[j])*(j-i-1)
    
    max_area = max(max_area, temp)
    
    if height[i]<=height[j]:
        i+=1
    else:
        j-=1
        
print(max_area)