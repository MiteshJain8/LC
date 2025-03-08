class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int l = 0;
        int cur = count(blocks.begin(), blocks.begin()+k, 'W');
        int res = cur;
        for (int r=k; r<blocks.size(); r++) {
            if (blocks[r] == 'W') cur++;
            if (blocks[l] == 'W') {
                cur--;
                res = min(res, cur);
            }
            l++;
        }
        return res;
    }
};