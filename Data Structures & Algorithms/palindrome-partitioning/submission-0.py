class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(start):
            if start >= len(s):
                res.append(part.copy())
                return

            for end in range(start, len(s)):
                if self.isPali(s, start, end):
                    part.append(s[start:end+1])
                    dfs(end+1)
                    part.pop()

        dfs(0)
        return res                


    def isPali(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start+1, end-1

        return True