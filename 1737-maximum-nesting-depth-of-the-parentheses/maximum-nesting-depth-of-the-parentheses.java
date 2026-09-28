class Solution {
    public int maxDepth(String s) {
        int cur = 0, res = 0, n = s.length();
        for (int i=0; i<n; i++) {
            if (s.charAt(i) == '(') {
                cur++;
                res = Math.max(res, cur);
            } else if (s.charAt(i) == ')') cur--;
        }
        return res;
    }
}