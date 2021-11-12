# Given a directed graph and two vertices ‘u’ and ‘v’, find the number of possible walks from ‘u’ to ‘v’ with exactly k edges modulo 109+7
# Day 59/100


def MinimumWalk(graph, u, v, k):
    V = len(graph)
    MOD = 1000000007

    count = [[[0 for k in range(k + 1)] for i in range(V)] for j in range(V)]

    for e in range(0, k + 1):

        for i in range(V):
            for j in range(V):

                if e == 0 and i == j:
                    count[i][j][e] = 1
                if e == 1 and graph[i][j] != 0:
                    count[i][j][e] = 1

                if e > 1:

                    for a in range(V):

                        if graph[i][a] != 0:
                            count[i][j][e] += count[a][j][e - 1]
                            count[i][j][e] = count[i][j][e] % MOD

    return count[u][v][k] % MOD


#  Driver Code Starts
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        n = int(input())
        graph = []
        for i in range(n):
            a = list(map(int, input().split()))
            graph.append(a)
        u, v, k = input().split()
        u = int(u)
        v = int(v)
        k = int(k)

        ans = MinimumWalk(graph, u, v, k)
        print(ans)
