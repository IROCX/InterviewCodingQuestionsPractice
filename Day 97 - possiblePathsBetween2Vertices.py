# Given a Directed Graph
# Count the total number of ways or paths that exist between two vertices in the directed graph
# Day 97 / 100


def countPaths(V, adj, source, destination):
    if source == destination:
        return 1
    return sum([countPaths(V, adj, child, destination) for child in adj[source]])


#  Driver Code Starts
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
        source, destination = map(int, input().split())
        print(countPaths(V, adj, source, destination))
