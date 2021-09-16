# arr = [1, 1, 1]
# k = 2
# ans = 2

from collections import defaultdict

def def_value():
    return 0

arr = list(map(int, input().split()))
k = int(input())

sum_map = defaultdict(def_value)
sum_map[0] = 1

count = 0
n = len(arr)

i = j = 0
current_sum = 0

for i in range(n):
    current_sum += arr[i]

    if current_sum - k in sum_map:
        count += sum_map[current_sum - k]

    sum_map[current_sum] += 1

print(count)
