class Solution {
public:
    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size(), q = queries.size();
        int curSum = 0, k = 0;
        vector<int> diff(n+1, 0);

        for (int idx = 0; idx < n; idx++) {
            while (curSum + diff[idx] < nums[idx]) {
                k++;
                if (k > q) return -1;

                int left = queries[k-1][0], right = queries[k-1][1], val = queries[k-1][2];

                if (right >= idx) {
                    diff[max(left, idx)] += val;
                    diff[right + 1] -= val;
                }
            }
            curSum += diff[idx];
        }
        return k;
    }
};