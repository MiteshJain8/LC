class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        vector<int> pre_process(n+1, 0);
        int cur_reduction = 0;
        for (vector<int>& q: queries) {
            pre_process[q[0]]++;
            pre_process[q[1]+1]--;
        }
        for (int i=0; i<n; i++) {
            cur_reduction += pre_process[i];
            if (cur_reduction < nums[i]) return false;
        }
        return true;
    }
};