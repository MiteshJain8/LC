class Solution {
public:
    int maxDepth(string s) {
        int cur = 0, res = 0, n = s.length();
        for (int i=0; i<n; i++) {
            if (s[i] == '(') {
                cur++;
                res = max(res, cur);
            } else if (s[i] == ')') {
                cur--;
            }
        }
        return res;
    }
};