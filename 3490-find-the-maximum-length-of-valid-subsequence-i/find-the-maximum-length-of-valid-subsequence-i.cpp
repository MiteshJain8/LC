class Solution {
public:
    int maximumLength(vector<int>& nums) {
        int c = nums[0] & 1, odd = 0, eve = 0, both = 0;
        for (int& num: nums) {
            if (num & 1) {
                odd++;
            } else {
                eve++;
            }
            if ((num & 1) == c) {
                both++;
                c = 1 - c;
            }
        }
        return max(max(odd, eve), both);
    }
};