# DFS + greedy algorithm problem
# Day 21/100

from sys import maxsize

class Solution:
    
    def dfs(self, k):
        if self.pipe_end[k] == 0:
            return k
        
        self.ans = min(self.dm[k], self.ans)
        
        return self.dfs(self.pipe_end[k])
        
    
    def util(self, mat, p):
        i = 0
        x = y = z = -1
        
        for i in range(p):
            x = mat[i][0]
            y = mat[i][1]
            z = mat[i][2]
            self.pipe_end[x] = y
            self.pipe_rec[y] = x
            self.dm[x] = z
            
        a1, a2 = self.pipe_end.count(0)-1,  self.pipe_rec.count(0) -1
        
        for i in range(1, n+1):
            if self.pipe_rec[i] == 0 and self.pipe_end[i]:
                self.ans = maxsize
                w = self.dfs(i)
                self.arr.append([i, w, self.ans])
        
        return a1, a2
                
        
    
    def solve(self, n, p ,a, b, d): 
        
        self.pipe_rec = [0]*(n+1)
        self.pipe_end = [0]*(n+1)
        self.dm = [0]*(n+1)
        self.ans = maxsize
        self.arr = []
        
        
        mat = []
        for i in range(p):
            mat.append([a[i], b[i], d[i]])
        # print(mat)
        
        a1, a2, = self.util(mat, p)

        return self.arr
        


#  Driver Code Starts

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        
        n,p = map(int,input().strip().split())
        a = []
        b = []
        d = []
        for i in range(p):
            x,y,z = map(int,input().strip().split())
            a.append(x)
            b.append(y)
            d.append(z)
            
        ob = Solution()
        ans = ob.solve(n, p, a, b, d)
        print(len(ans))
        for i in ans:
            print(str(i[0])+" "+str(i[1])+" "+str(i[2]))
