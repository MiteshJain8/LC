class Solution {
    public int minimumRecolors(String blocks, int k) {
        int l = 0, cur = 0;
        for (int i=0; i<k; i++) {
            if (blocks.charAt(i) == 'W') cur++;
        }
        int res = cur;
        for (int r=k; r<blocks.length(); r++) {
            if (blocks.charAt(r) == 'W') cur++;
            if (blocks.charAt(l) == 'W') {
                cur--;
                res = Math.min(res, cur);
            }
            l++;
        }
        return res;
    }
}