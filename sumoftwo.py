# approach is using hashmap equivalent in python - defaultdict

# arr1 = [1,2,3,4,5]
# arr2 = [1,2,6,8,9]
# sum = 12
# ans = 4, 8 -> True

from collections import defaultdict

def default():
    return 0

# return boolean
def sumOfTwo(arr1, arr2, v):
    d = defaultdict(default)
    for i in range(len(arr1)):
        d[arr1[i]]=1
    for i in range(len(arr2)):
        if d[v-arr2[i]]==1:
            return True
    return False


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
v = int(input())
print(sumOfTwo(arr1, arr2, v))