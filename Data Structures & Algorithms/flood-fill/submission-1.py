class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        M, N = len(image), len(image[0])
        def dfs(r, c, org):
            if not( 0<= r < M) or not (0 <= c < N) or image[r][c] != org:
                return 

            image[r][c] = color

           
            dfs(r+1, c, org)
            dfs(r-1, c , org)
            dfs(r, c+1, org)
            dfs(r, c-1, org)

            
        dfs(sr, sc, image[sr][sc])
        return image