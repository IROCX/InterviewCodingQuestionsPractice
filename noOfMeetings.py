# number of meating that can be held with given start and end timing provided that end of one meeting cannot be same as start of next meeting
# Day 2/100

n = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))

intervals = zip(start, end)
intervals = sorted(intervals, key=lambda x: x[1])


count = 1
i = 0
j = 1
while j < n:
    if intervals[i][1] <= intervals[j][0]:
        print(intervals[i])
        count += 1
        i = j
        j += 1
    else:
        j += 1



print(intervals, count)
