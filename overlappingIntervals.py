# given list of intervals - merge all overlapping intervals
# Day 27/100


def overlappedInterval(Intervals):

    Intervals.sort(key=lambda x: x[0])

    i = 1
    while i < len(Intervals):

        if Intervals[i - 1][1] >= Intervals[i][0]:

            if Intervals[i - 1][1] >= Intervals[i][1]:
                Intervals.pop(i)
            else:
                Intervals[i - 1][1] = Intervals[i][1]
                Intervals.pop(i)
        else:
            i += 1

    return Intervals


#  Driver Code Starts

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().strip().split()))
        Intervals = []
        j = 0
        for i in range(n):
            x = a[j]
            j += 1
            y = a[j]
            j += 1
            Intervals.append([x, y])
        ans = overlappedInterval(Intervals)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()
