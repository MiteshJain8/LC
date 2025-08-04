class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        unordered_map<int, int> mp;
        int l = 0, res = 0, n = fruits.size();
        for (int r = 0; r < n; r++) {
            mp[fruits[r]]++;
            if (mp.size() <= 2) res = max(res, r - l + 1);
            else {
                while (mp.size() > 2) {
                    if (!--mp[fruits[l]]) mp.erase(fruits[l]);
                    l++;
                }
            }
        }
        return res;
    }
};