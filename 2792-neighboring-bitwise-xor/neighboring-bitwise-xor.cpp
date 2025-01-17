class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        int Xor = 0;
        for (int num : derived) Xor ^= num;
        return !Xor;
    }
};