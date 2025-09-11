class Solution:
    def sortVowels(self, s: str) -> str:
        swaps, indices = [], []
        lst = list(s)
        vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        for i, c in enumerate(lst):
            if c in vowels:
                swaps.append(c)
                indices.append(i)
        swaps.sort()
        for i, c in zip(indices, swaps):
            lst[i] = c

        return "".join(lst)