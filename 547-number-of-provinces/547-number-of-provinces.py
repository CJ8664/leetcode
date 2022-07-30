class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_province = len(isConnected)
        par = [i for i in range(num_province)]
        rank = [1 for _ in range(num_province)]
        
        def find_par(a):
            while a != par[a]:
                par[a] = par[par[a]]
                a = par[a]
            return a
                
        def union(a, b):
            p_a, p_b = find_par(a), find_par(b)
            if p_a == p_b:
                return 0

            if rank[p_a] > rank[p_b]:
                par[p_b] = p_a
                rank[p_a] += rank[p_b]
            else:
                par[p_a] = p_b
                rank[p_b] += rank[p_a]
            return 1
                
        
        for l in range(len(isConnected)):
            for r in range(len(isConnected[0])):
                if isConnected[l][r] == 1:
                    num_province -= union(l, r)
        return num_province
        