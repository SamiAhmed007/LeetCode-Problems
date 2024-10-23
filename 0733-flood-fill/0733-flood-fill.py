class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m , n = len(image), len(image[0])
        target = color
        curr_color = image[sr][sc] 
        visited = []
        for i in range(m):
            l = []
            for j in range(n):
                l.append(False)
            visited.append(l)
        
        def dfs(i, j, curr_color, target, visited):
            if 0<=i<m and 0<=j<n and visited[i][j]==True:
                return
            if 0<=i<m and 0<=j<n and curr_color != image[i][j]:
                return 
            if 0<=i<m and 0<=j<n and curr_color == image[i][j] and not visited[i][j]:
                visited[i][j] = True
                image[i][j] = target  
                # if visited[]
                dfs(i+1, j, curr_color, target, visited)
                dfs(i, j+1, curr_color, target, visited)
                dfs(i-1, j, curr_color, target, visited)
                dfs(i, j-1, curr_color, target, visited)
       
        dfs(sr, sc, curr_color, target, visited)

        return image 












