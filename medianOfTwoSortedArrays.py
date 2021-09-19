# median of two sorted arrays - linear approach
# Day 5/100 

m = input()
array1 = [int(x) for x in input().split()]
n = input()
array2 = [int(x) for x in input().split()]


l1, l2 = len(array1), len(array2)

l = l1 + l2

if l & 1:
    med = [l // 2]
else:
    med = [l // 2 - 1, l // 2]

i = 0
j = 0

meds = [0, 0]
flag = 0

ele = 0
if l1 == 0 and l2 == 0:
    print(0)
elif l1 == 0:
    if l2 & 1:
        print(array2[l2 // 2])
    else:
        print((array2[l2 // 2 - 1] + array2[(l2 // 2)]) / 2)
elif l2 == 0:
    if l1 & 1:
        print(array1[l1 // 2])
    else:
        print((array1[l1 // 2 - 1] + array1[(l1 // 2)]) / 2)

else:
    while i < l1 and j < l2:
        if array1[i] <= array2[j]:
            if ele == med[0]:
                meds[0] = array1[i]
                if len(med) != 2:
                    flag = 1
                    break

            if len(med) == 2 and ele == med[1]:
                meds[1] = array1[i]
                flag = 1
                break

            i += 1
            ele += 1
        else:

            if ele == med[0]:
                meds[0] = array2[j]
                if len(med) != 2:
                    flag = 1
                    break

            if len(med) == 2 and ele == med[1]:
                meds[1] = array2[j]
                flag = 1
                break

            j += 1
            ele += 1

    if flag == 0:
        while i < l1:

            if ele == med[0]:
                meds[0] = array1[i]
                if len(med) != 2:
                    flag = 1
                    break

            if len(med) == 2 and ele == med[1]:
                meds[1] = array1[i]
                flag = 1
                break

            i += 1
            ele += 1

    if flag == 0:
        while j < l2:

            if ele == med[0]:
                meds[0] = array2[j]
                if len(med) != 2:
                    flag = 1
                    break

            if len(med) == 2 and ele == med[1]:
                meds[1] = array2[j]
                flag = 1
                break

            j += 1
            ele += 1

    if len(med) == 2:
        res = sum(meds) / 2
        if res == int(res):
            print(int(res))
        else:
            print(res)
    else:
        print(meds[0])

