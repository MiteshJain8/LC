class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def is_hamming_dist_one(s1, s2):
            diff = 0
            for i,j in zip(s1,s2):
                if i != j:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1
            
        n = len(words)
        dp = [1] * n
        parent = [-1] * n
        sub_seq_idx = 0
        longest_seq = 1
        for i in range(1,n):
            for j in range(i):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and is_hamming_dist_one(words[i], words[j]):
                    if dp[i] < dp[j] + 1:
                        parent[i] = j
                        dp[i] = dp[j] + 1
                        if longest_seq < dp[i]:
                            sub_seq_idx = i
                            longest_seq = dp[i]
            
        res = []
        while sub_seq_idx != -1:
            res.append(words[sub_seq_idx])
            sub_seq_idx = parent[sub_seq_idx]

        return res[::-1]