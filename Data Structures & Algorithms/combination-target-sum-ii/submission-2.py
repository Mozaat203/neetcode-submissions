class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs( subset, index, total):
            if total == target:
                res.append(subset.copy())
                return
            
            if total > target or index == len(candidates):
                return

            subset.append(candidates[index])

            dfs(subset, index +1 , total +candidates[index] )
            
            subset.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1

            dfs(subset , index + 1, total)

        dfs([],0,0)
        return res






            
