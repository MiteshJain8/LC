class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vow = cons = False
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        for c in word:
            if not c.isalnum():
                return False
            elif c in vowels:
                vow = True
            elif not c.isdigit():
                cons = True

        return True if cons and vow else False