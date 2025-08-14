class Solution {
public:
    string largestGoodInteger(string num) {
        vector<string> vals = {"999", "888", "777", "666", "555", "444", "333", "222", "111", "000"};
        for (string s: vals) if (num.find(s) != string::npos) return s;
        return "";
    }
};