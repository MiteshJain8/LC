class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long res = 0;
        int l = -1;
        for (int r=0; r<nums.size(); ++r) {
            if (nums[r]) l = r;
            else res += (r-l);
        }
        return res;
    }
};