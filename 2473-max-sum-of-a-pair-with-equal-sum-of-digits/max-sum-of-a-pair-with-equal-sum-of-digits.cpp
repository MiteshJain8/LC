class Solution {
public:
    int maximumSum(vector<int>& nums) {
        int prefix[82] = {0};
        int n = nums.size(), res = -1;
        for (int i = 0; i < n; ++i) {
            int num = nums[i], dig = 0;
            while (num) {
                dig += num % 10;
                num /= 10;
            }
            if (prefix[dig]) {
                res = max(res, nums[i] + prefix[dig]);
                prefix[dig] = max(nums[i], prefix[dig]);
            } else {
                prefix[dig] = nums[i];
            }
        }
        return res;
    }
};