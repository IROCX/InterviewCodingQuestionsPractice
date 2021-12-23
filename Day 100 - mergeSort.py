# Given an array, its starting position l and its ending position r
# Sort the array using merge sort algorithm
# Day 100 / 100


def merge(arr, l, m, r):
    temp = [0 for i in range(r - l + 1)]
    k = 0
    i = l
    j = m + 1
    while i <= m and j <= r:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while j <= r:
        temp[k] = arr[j]
        k += 1
        j += 1
    while i <= m:
        temp[k] = arr[i]
        k += 1
        i += 1
    arr[l : r + 1] = temp


def mergeSort(arr, l, r):

    if l == r:
        return
    else:
        mid = (l + r) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, mid, r)


#  Driver Code Starts

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        mergeSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
