class Solution:
    def minimumLength(self, s: str) -> int:
        st, k = Counter(s), 0
        for j in st.values():
            if j & 1:
                k += 1
            else:
                k += 2
        return k