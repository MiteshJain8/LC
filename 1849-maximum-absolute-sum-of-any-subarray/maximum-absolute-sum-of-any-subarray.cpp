class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int curSum = 0, minPre = 0, maxPre = 0, res = 0;
        for (int num: nums) {
            curSum += num;
            res = max(res, max(abs(curSum-maxPre), abs(curSum-minPre)));
            maxPre = max(maxPre, curSum);
            minPre = min(minPre, curSum);
        }
        return res;
    }
};