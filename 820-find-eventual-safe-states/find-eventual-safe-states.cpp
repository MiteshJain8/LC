class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        unordered_map<int, bool> safe;
        vector<int> res;

        function<bool(int)> dfs = [&](int i) {
            if (safe.find(i) != safe.end()) {
                return safe[i];
            }
            safe[i] = false;
            for (int nei : graph[i]) {
                if (!dfs(nei)) {
                    return false;
                }
            }
            safe[i] = true;
            return true;
        };

        for (int i = 0; i < n; ++i) {
            if (dfs(i)) {
                res.push_back(i);
            }
        }
        return res;
    }
};