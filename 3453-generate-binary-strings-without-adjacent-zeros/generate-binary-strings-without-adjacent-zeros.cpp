class Solution {
public:
    vector<string> backtrack(int n, int i, string subs) {
        vector<string> res;
        if (i == n-1) {
            res.push_back(subs);
            return res;
        }
        if (subs[i] == '0') {
            vector<string> ans1 = backtrack(n, i+1, subs+'1');
            res.insert(res.end(), ans1.begin(), ans1.end());
        } else {
            vector<string> ans1 = backtrack(n, i+1, subs+'1');
            res.insert(res.end(), ans1.begin(), ans1.end());
            vector<string> ans2 = backtrack(n, i+1, subs+'0');
            res.insert(res.end(), ans2.begin(), ans2.end());
        }
        return res;
    }

    vector<string> validStrings(int n) {
        vector<string> res1, res2;
        res1 = backtrack(n, 0, "1"); 
        res2 = backtrack(n, 0, "0");
        res1.insert(res1.end(), res2.begin(), res2.end());
        return res1;
    }
};