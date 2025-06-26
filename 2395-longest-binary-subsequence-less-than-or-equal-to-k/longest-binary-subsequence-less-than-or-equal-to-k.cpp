class Solution {
public:
    int longestSubsequence(string s, int k) {
        reverse(s.begin(), s.end());
        int power = 1, res = 0;
        for (char& c: s) {
            if (c == '0') {
                res++;
            } else if (power <= k) {
                k -= power;
                res++;
            }
            if (power <= k) power *= 2;
        }
        return res;
    }
};