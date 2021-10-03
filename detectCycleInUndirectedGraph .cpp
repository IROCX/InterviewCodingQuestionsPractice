// detect cycle in an undirected graph
// Day 19 / 100

#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
  
  
    bool isCyclic(vector<int> adj[], vector<int> visited, int c){
        if(visited[c] == 2){
            return 1;
        }
        
        visited[c] = 1;
        bool flag = false;
        for(int i = 0  ; i < adj[c].size() ; i++){
            if (visited[adj[c][i]] == 1){
                visited[adj[c][i]] = 2;
            }else{
                flag = isCyclic(adj, visited, adj[c][i]);
                if (flag){
                    return 1;
                }
            }
        }
        return 0;
    }
    // Function to detect cycle in an undirected graph.
    bool isCycle(int V, vector<int> adj[]) {
        
        vector<int> visited(V, 0);
        bool flag = 0;
        for(int i = 0 ; i < V ; i++){
            visited[i] = 1;
            for(int j = 0 ; j < adj[i].size() ; j++){
                flag = isCyclic(adj, visited, adj[i][j]);
                if (flag){
                    return 1;
                }
            }
            visited[i] = 0;
        }
        return 0;
    }
};

// Driver Code
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int V, E;
        cin >> V >> E;
        vector<int> adj[V];
        for (int i = 0; i < E; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        Solution obj;
        bool ans = obj.isCycle(V, adj);
        if (ans)
            cout << "1\n";
        else
            cout << "0\n";
    }
    return 0;
}