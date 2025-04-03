class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long res = 0, maxi = 0, maxDiff = 0;
        for (int& num: nums) {
            res = max(res, maxDiff * num);
            maxDiff = max(maxDiff, maxi - num);
            maxi = max(maxi, (long long)num);
        }
        return res;
    }
};