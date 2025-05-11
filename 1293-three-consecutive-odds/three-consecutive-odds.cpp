class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int c = 3;
        for (int& num: arr) {
            if (num & 1) {
                c--;
                if (!c) return true;
            } else c = 3;
        }
        return false;
    }
};