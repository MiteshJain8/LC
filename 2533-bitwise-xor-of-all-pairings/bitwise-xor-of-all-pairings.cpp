class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int res = 0;
        if (nums1.size() & 1) 
            res = std::accumulate(nums2.begin(), nums2.end(), 0, std::bit_xor<int>());
        if (nums2.size() & 1) 
            res = std::accumulate(nums1.begin(), nums1.end(), res, std::bit_xor<int>());
        return res;
    }
};