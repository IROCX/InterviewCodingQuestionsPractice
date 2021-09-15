# Kadane's Algorithm

# arr = [-2,2,5,-11,6]
# ans = 7
# sub-array = elements have to be consecutive

# input array
arr = list(map(int, input().split()))
n = len(arr)

# vars for current_sum and max_sum
max_sum = arr[0]
current_sum = arr[0]

for i in range(1, n):

    # checking the max of current_sum+arr[i] & arr[i]
    current_sum = max(current_sum+arr[i], arr[i])

    # updating max_sum achieved so far
    max_sum = max(max_sum, current_sum)

print(max_sum)
