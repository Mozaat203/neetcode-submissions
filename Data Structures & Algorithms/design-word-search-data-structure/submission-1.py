class TrieNode:
    def __init__(self):
        self.children = {}
        self.word=False

class WordDictionary:

    def __init__(self):
        self.root= TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]

        current.word = True

    def search(self, word: str) -> bool:
        def dfs( x , current):
            for i in range(x , len(word)):
                c = word[i]
                
                if c == ".":
                    for child in current.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if c not in current.children:
                        return False
                    current = current.children[c]

            return current.word
        return dfs(0 , self.root)