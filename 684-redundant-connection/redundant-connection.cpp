class DSU {
public:
    vector<int> parent;

    DSU(int& n) {
        parent.resize(n, -1);
    }

    void unionSet(int& pa, int& pb) {
        if (parent[pb] < parent[pa]) {
            parent[pb] += parent[pa];
            parent[pa] = pb;
        } else {
            parent[pa] += parent[pb];
            parent[pb] = pa;
        }
    }

    int find(int& u) {
        if (parent[u] < 0) return u;
        return parent[u] = find(parent[u]);
    }
};

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        DSU dsu(n);
        for (vector<int>& edge: edges) {
            int pa = dsu.find(edge[0]), pb = dsu.find(edge[1]);
            if (pa == pb) return edge;
            else dsu.unionSet(pa,pb);
        }
        return {};
    }
};