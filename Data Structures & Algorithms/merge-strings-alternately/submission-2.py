class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = 0 , 0
        newString = []
        while l1 < len(word1) and l2 < len(word2):
            newString.append(word1[l1])
            newString.append(word2[l2])

            l1+=1
            l2+=1

        newString.append(word1[l1:])
        newString.append(word2[l2:])

        return "".join(newString)