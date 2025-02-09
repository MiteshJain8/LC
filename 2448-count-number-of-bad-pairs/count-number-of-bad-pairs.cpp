class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        unordered_map<int, int> hmap;
        int n = nums.size();
        long long res = static_cast<long long>(n) * (n - 1) / 2;
        for (int i = 0; i < n; ++i) {
            hmap[nums[i] - i]++;
        }
        for (const auto& [key, cnt] : hmap) {
            res -= static_cast<long long>(cnt) * (cnt - 1) / 2;
        }
        return res;
    }
};