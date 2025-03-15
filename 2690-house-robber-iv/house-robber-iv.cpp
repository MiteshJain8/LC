class Solution {
public:
    bool isPossible(vector<int>& nums, int k, int val) {
        int cur = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] <= val) {
                cur++;
                if (cur == k) return true;
                i++;
            }
        }
        return false;
    }

    int minCapability(vector<int>& nums, int k) {
        set<int> unique_nums(nums.begin(), nums.end());
        vector<int> sizes(unique_nums.begin(), unique_nums.end());
        int left = 0, right = sizes.size() - 1, res = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (isPossible(nums, k, sizes[mid])) {
                res = sizes[mid];
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }
};