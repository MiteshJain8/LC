class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        unordered_map<int,int> hmap;
        int n = nums.size(), res = 0;
        for (int i=0; i<n-1; i++) {
            for (int j=i+1; j<n; j++) {
                hmap[nums[i]*nums[j]]++;
            }
        }
        for (auto& itr: hmap) {
            res += 4*(itr.second)*(itr.second-1);
        }
        return res;
    }
};