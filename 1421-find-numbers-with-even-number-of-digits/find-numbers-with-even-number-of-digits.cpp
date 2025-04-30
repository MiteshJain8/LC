class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int res = 0;
        for (int& num: nums)
            if ((to_string(num).length() & 1) == 0)
                res++;
        return res;
    }
};