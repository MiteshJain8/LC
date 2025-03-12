class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int firstNonNeg = lower_bound(nums.begin(), nums.end(), 0) - nums.begin();
        int firstPos = lower_bound(nums.begin(), nums.end(), 1) - nums.begin();
        int neg = firstNonNeg, pos = nums.size() - firstPos;
        return max(pos, neg);
    }
};