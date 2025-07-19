class Node {
public:
    int val;
    unordered_map<string, Node*> child;
    bool isEnd = false;
};

class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        Node* head = new Node;
        for (auto& s : folder) {
            Add(s, head);
        }
        vector<string> res;
        dfs(head, "", res);
        return res;
    }

private:
    void Add(string& s, Node* head) {
        Node* cur = head;
        string folder = "";
        for (int i = 1; i <= s.size(); i++) {
            if (i == s.size() || s[i] == '/') {
                if (cur->child.find(folder) == cur->child.end())
                    cur->child[folder] = new Node();
                cur = cur->child[folder];
                folder = "";
            } else {
                folder += s[i];
            }
        }
        cur->isEnd = true;
    }
    void dfs(Node* cur, string ans, vector<string>& res) {
        // if (!cur) return;
        if (cur->isEnd) {
            res.push_back(ans);
            return;
        }
        for (auto& p : cur->child) {
            string folder = p.first;
            Node* tmp = p.second;
            dfs(tmp, ans + '/' + folder, res);
        }
    }
};
