class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int M = 1e9 + 7, n = nums.size();
        vector<int> power(n,1);
        for (int i=1; i<n; ++i) power[i] = (power[i-1] * 2) % M;
        int i = 0, j = n-1, res = 0;
        while (i <= j) {
            if (nums[i] + nums[j] <= target) {
                res = (res + power[j-i] % M) % M;
                i++;
            } else j--;
        }
        return res;
    }
};