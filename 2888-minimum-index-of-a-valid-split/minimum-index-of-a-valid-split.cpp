class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        int votes = 0, candidate = -1, n = nums.size();
        for (int num: nums) {
            if (!votes) {
                candidate = num;
                votes++;
            } else {
                if (candidate == num) votes++;
                else votes--;
            }
        }
        votes = 0;
        for (int j=0; j<n; j++) {
            if (nums[j] == candidate) {
                votes++;
                if (2*votes > j+1) {
                    if (2*count(nums.begin()+j+1, nums.end(), candidate) > n-j-1) return j;
                    else return -1;
                }
            }
        }
        return -1;
    }
};