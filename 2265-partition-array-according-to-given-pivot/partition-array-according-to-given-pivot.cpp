class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int j = 0;
        vector<int> res(nums);
        sort(res.begin(),res.end());
        int idx = upper_bound(res.begin(), res.end(), pivot) - res.begin();
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] < pivot) {
                res[j] = nums[i];
                j++;
            } else if (nums[i] > pivot) {
                res[idx] = nums[i];
                idx++;
            }
        }
        return res;
    }
};