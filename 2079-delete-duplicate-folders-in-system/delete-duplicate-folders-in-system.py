class Trie:
    def __init__(self):
        self.serial = ""
        self.children = {}

class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        root = Trie()

        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]

        freq = {}

        def construct(node):
            if not node.children:
                return

            v = []
            for folder, child in node.children.items():
                construct(child)
                v.append(folder + "(" + child.serial + ")")
            
            v.sort()
            node.serial = "".join(v)
            
            freq[node.serial] = freq.get(node.serial, 0) + 1

        construct(root)

        ans = []
        path = []

        def operate(node):
            if node.serial in freq and freq[node.serial] > 1:
                return
            
            if path:
                ans.append(list(path))
            
            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()

        operate(root)
        return ans