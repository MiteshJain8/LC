class Solution {
public:
    int maximum69Number (int num) {
        string s = to_string(num);
        int pos = s.find("6");
        if (pos != string::npos) {
            s.replace(pos, 1, "9");
        }
        return stoi(s);
    }
};