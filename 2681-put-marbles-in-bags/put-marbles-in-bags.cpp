class Solution {
public:
    long long putMarbles(vector<int>& weights, int k) {
        int n = weights.size();
        if (k == 1 || k == n) return 0;
        for (int i=0; i<n-1; i++) weights[i] += weights[i+1];
        weights.pop_back();
        sort(weights.begin(),weights.end());
        long long res = 0;
        for (int i=0; i<k-1; i++) res += weights[n-2-i] - weights[i];
        return res;
    }
};