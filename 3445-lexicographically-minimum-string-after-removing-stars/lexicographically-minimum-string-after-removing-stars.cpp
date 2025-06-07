class Solution {
public:
    string clearStars(string s) {
        vector<char> res(s.begin(), s.end());
        int n = s.length();
        priority_queue<pair<char, int>, vector<pair<char, int>>, greater<pair<char, int>>> pq;
        
        for (int i = 0; i < n; i++) {
            if (s[i] == '*') {
                auto [ch, idx] = pq.top();
                pq.pop();
                res[-idx] = '\0';
                res[i] = '\0';
            } else {
                pq.push({s[i], -i});
            }
        }
        
        string result;
        for (char c : res) {
            if (c != '\0') {
                result += c;
            }
        }
        return result;
    }
};