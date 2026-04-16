class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res =[]
        part= []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(index, part):
            if len(part) == len(digits):
                res.append(part)
                return
            for ch in digitToChar[digits[index]]:
                dfs(index+1, part+ch)

        if digits:
            dfs(0, "")

        return res


