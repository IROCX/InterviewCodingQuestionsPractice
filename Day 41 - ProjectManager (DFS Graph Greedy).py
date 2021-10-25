# An IT company is working on a large project.
# The project is broken into N modules and distributed to different teams. Each team can work in parallel.
# The amount of time (in months) required to complete each module is given in an array duration[ ] i.e. time needed to complete ith module is duration[i] months.
# You are also given M dependencies such that for each i(1 ≤ i ≤ M)  dependencies[i][1]th module can be started after dependencies[i][0]th module is completed.
# As the project manager, compute the minimum time required to complete the project.

# DFS | GRAPH | GREEDY
# Day 41/100


def minTime(deps, dur, n, m):

    if m == 0:
        return max(dur)

    d = {i: 0 for i in range(n)}
    adj = {i: [] for i in range(n)}
    mindur = [dur[i] for i in range(n)]

    for i in range(m):
        d[deps[i][1]] += 1
        adj[deps[i][0]].append(deps[i][1])

    q = []

    for i in d.keys():
        if d[i] == 0:
            q.append(i)

    processed = []
    while q:
        temp = q.pop(0)
        processed.append(temp)
        for i in adj[temp]:
            mindur[i] = max(mindur[i], dur[i]+mindur[temp])
            d[i] -= 1
            if d[i] == 0:
                q.append(i)

    if len(processed) == n:
        return max(mindur)
    return -1


#  Driver Code Starts

for _ in range(0, int(input())):
    n, m = map(int, input().split())
    duration = list(map(int, input().split()))
    dependency = []
    for i in range(0, m):
        l = list(map(int, input().split()))
        dependency.append(l)

    print(minTime(dependency, duration, n, m))
