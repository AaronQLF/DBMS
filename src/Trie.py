class TrieNode: 
    def __init__(self): 
        self.Children = {}
        self.isLeaf = False

class Trie: 
    def __init__(self): 
        self.root = TrieNode()
    
    def insert(self, word):
        c = self.root
        for w in word: 
            if w not in c.Children: 
                c.Children[w] = TrieNode()
            c = c.Children[w]
        c.isLeaf = True

    def delete(self, word): 
        def dfs(root: TrieNode, depth=0): 
            if not root: 
                return None
            if depth == len(word): 
                if root.isLeaf: 
                    root.isLeaf = False
                if len(root.Children) == 0: 
                    return None
                return root
            char = word[depth]
            root.Children[char] = dfs(root.Children.get(char), depth + 1)
            if not root.Children[char] and not root.isLeaf:
                del root.Children[char]
                if len(root.Children) == 0:
                    return None
            return root
        
        dfs(self.root)

    def get(self, node):
        r = []
        def rfs(root: TrieNode, cs):
            nonlocal r
            if root.isLeaf:
                r.append(cs)
            for i in root.Children:
                rfs(root.Children[i], cs + i)
        rfs(node, "")
        return r

    def closest(self, word):
        c = self.root
        for i, w in enumerate(word):
            if w not in c.Children:
                return word[:i] + list(c.Children.keys())[0] if c.Children else []
            c = c.Children[w]
        return [word + e for e in self.get(c)]
    
    def contains(self, word): 
        c = self.root
        for w in word: 
            if w not in c.Children: 
                return False
            c = c.Children[w]
        return c.isLeaf