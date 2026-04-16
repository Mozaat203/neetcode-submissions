class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        M, N = len(image), len(image[0])
        dirs = [1,0,-1,0,1]
        def dfs(r, c, org):
            if not( 0<= r < M) or not (0 <= c < N) or image[r][c] != org:
                return 

            image[r][c] = color

            for i in range(4):
                dfs(r+dirs[i], c+ dirs[i+1], org)

            
        dfs(sr, sc, image[sr][sc])
        return image