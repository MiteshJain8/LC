class Solution {
public:
    int M = 1e9+7;
    int lengthAfterTransformations(string s, int t) {
        vector<int> mp(26);
        for(char& c: s) mp[c-'a']++;
        for(int i=0; i<t; i++) {
            int z = mp[25];
            for(int j=25; j>0; j--) mp[j] = mp[j-1];
            mp[0] = z;
            mp[1] = (mp[1] + z) % M;
        }
        int res = 0;
        for (int& ele : mp) res = (res + ele) % M;
        return res;
    }
};