class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        lst = [i for i in range(1, len(isConnected)+1)]
        province = 0
        n = len(isConnected[0])

        def dfs(isConnected, lst, first, province):
            if len(lst) <= 0:
                return province
            
            lst.remove(first)
            for i in range(n):
                if isConnected[first-1][i] == 1 and (i+1 != first) and (i+1 in lst):
                    dfs(isConnected, lst, i+1, province)
            return

        while (len(lst) > 0):
                province+=1
                dfs(isConnected, lst, lst[0], province)
        return province
        # return dfs(isConnected, lst, lst[0], province)

        
