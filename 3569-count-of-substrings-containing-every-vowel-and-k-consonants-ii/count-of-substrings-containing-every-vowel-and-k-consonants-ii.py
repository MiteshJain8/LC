class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def count_at_least_k_consonants(k: int) -> int:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            vowel_count = {}
            consonant_count = 0
            start = 0
            valid_substrings = 0

            for end in range(len(word)):
                if word[end] in vowels:
                    vowel_count[word[end]] = vowel_count.get(word[end], 0) + 1
                else:
                    consonant_count += 1

                while len(vowel_count) == 5 and consonant_count >= k:
                    valid_substrings += len(word) - end
                    if word[start] in vowels:
                        vowel_count[word[start]] -= 1
                        if vowel_count[word[start]] == 0:
                            del vowel_count[word[start]]
                    else:
                        consonant_count -= 1
                    start += 1

            return valid_substrings

        return count_at_least_k_consonants(k) - count_at_least_k_consonants(k + 1)