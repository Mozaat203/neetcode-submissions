class Solution:
    def decodeString(self, s: str) -> str:
        charStack = []
        countStack = []
        curr = ""
        currMulti = 0
        

        for token in s:
            if token.isdigit():
                currMulti = currMulti * 10 + int(token)

            elif token == "[":
                countStack.append(currMulti)
                charStack.append(curr)
                curr = ""
                currMulti = 0

            elif token == "]":
                temp = curr
                curr = charStack.pop()
                count = countStack.pop()
                curr += temp * count

            else:
                curr += token

        return curr
