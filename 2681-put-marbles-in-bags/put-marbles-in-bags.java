class Solution {
    public long putMarbles(int[] weights, int k) {
        int n = weights.length;
        if (k == 1 || n == k) return 0;
        int[] costs = new int[n-1];
        for (int i = 0; i < n - 1; ++i) {
            costs[i] = weights[i] + weights[i + 1];
        }
        Arrays.sort(costs);
        long res = 0l;
        for (int i = 0; i < k - 1; ++i) {
            res += costs[n - 2 - i] - costs[i];
        }
        return res;
    }
}