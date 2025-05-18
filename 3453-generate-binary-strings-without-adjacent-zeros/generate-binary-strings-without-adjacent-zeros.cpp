class Solution {
public:
    vector<string> res;
    void backtrack(int n, int i, string& subs) {
        if (i == n-1) {
            res.push_back(subs);
            return;
        }
        subs.push_back('1');
        backtrack(n, i+1, subs);
        subs.pop_back();
        if (subs[i] == '1') {
            subs.push_back('0');
            backtrack(n, i+1, subs);
            subs.pop_back();
        }
    }

    vector<string> validStrings(int n) {
        string a="1", b="0";
        backtrack(n, 0, a); 
        backtrack(n, 0, b);
        return res;
    }
};