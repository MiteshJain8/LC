class Solution {
    public int minZeroArray(int[] nums, int[][] queries) {
        int n = nums.length, q = queries.length;
        int curSum = 0, k = 0;
        int[] diff = new int[n+1];

        for (int idx = 0; idx < n; idx++) {
            while (curSum + diff[idx] < nums[idx]) {
                k++;
                if (k > q) return -1;

                int left = queries[k-1][0], right = queries[k-1][1], val = queries[k-1][2];

                if (right >= idx) {
                    diff[Math.max(left, idx)] += val;
                    diff[right + 1] -= val;
                }
            }
            curSum += diff[idx];
        }
        return k;
    }
}