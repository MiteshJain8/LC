class Solution {
public:
    int minimumLength(string s) {
        vector<int> st(26);
        for (char& c: s)    st[c-'a']++;
        int k = 0;
        for (int& e: st)   e ? ((e & 1) ? k++ : k += 2) : 0;
        return k;
    }
};