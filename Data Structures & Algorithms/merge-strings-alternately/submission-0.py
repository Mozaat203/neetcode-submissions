class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = 0, 0
        string = ""
        finish = 0

        while finish == 0:
            if (l2 < len(word2)  and l1 < len(word1) ):
                string += word1[l1]
                string += word2[l2]
                l1 += 1
                l2 += 1

            elif (l1 >= len(word1) ):
                while (l2 < len(word2)):
                    string += word2[l2]
                    l2 += 1
                finish = 1

            elif (l2 >= len(word2)):
                while (l1 < len(word1)):
                    string += word1[l1]
                    l1 += 1
                finish = 1

        return string