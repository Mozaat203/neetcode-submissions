class Solution:
    def decodeString(self, s: str) -> str:
        stack = []


        for token in s:
            if token != "]":
                stack.append(token)

            else:
                temporalString = ""
                
                while stack[-1] != "[":
                    temporalString = stack.pop() + temporalString

                stack.pop()

                multiplier = ""

                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier

                stack.append(int(multiplier) * temporalString)


        return "".join(stack)