# Given a weighted, undirected and connected graph of V vertices and E edges.
# The task is to find the sum of weights of the edges of the Minimum Spanning Tree.
# Day 40/100

from sys import maxsize


class Solution:

    def spanningTree(self, V, adj):
        # code here
        vis = [0]*V

        nv = V
        ne = len(adj)//2
        if nv == ne + 1:
            sumx = 0
            for i in range(ne):
                sumx += adj[i*2][0][1]
            return sumx

        w = [maxsize]*V
        w[0] = 0
        st = set()

        while len(st) < V:
            mn = maxsize
            ind = -1
            for i in range(V):
                if w[i] < mn and i not in st:
                    ind = i
                    mn = w[i]
            st.add(ind)
            for j in adj[ind]:
                if j[0] not in st:
                    if w[j[0]] > j[1]:
                        w[j[0]] = j[1]
        return sum(w)


#  Driver Code Starts

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))
