class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        original = set(wordlist)
        capitalization = defaultdict(str)
        vowel_error = defaultdict(str)
        aeiou = set(['a','e','i','o','u'])
        for i,w in enumerate(wordlist):
            if w.lower() not in capitalization:
                capitalization[w.lower()] = i
        for k,v in capitalization.items():
            word = list(k)
            for i,c in enumerate(word):
                if c in aeiou:
                    word[i] = 'a'
            word = "".join(word)
            if (word not in vowel_error) or (vowel_error[word] > v):
                vowel_error[word] = v

        ans = [""] * len(queries)
        for i,q in enumerate(queries):
            if q in original:
                ans[i] = q
            else:
                word = q.lower()
                if word in capitalization:
                    ans[i] = wordlist[capitalization[word]]
                else:
                    word = list(word)
                    for j,c in enumerate(word):
                        if c in aeiou:
                            word[j] = 'a'
                    word = "".join(word)
                    if word in vowel_error:
                        ans[i] = wordlist[vowel_error[word]]
        return ans