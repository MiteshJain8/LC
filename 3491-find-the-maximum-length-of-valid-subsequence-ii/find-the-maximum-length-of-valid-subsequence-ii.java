class Solution {
    public int maximumLength(int[] nums, int k) {
        int n = nums.length;
        int[][] dp = new int[n][k];
        for (int[] row: dp) Arrays.fill(row, 1);
        int length = 1;
        for (int i=0; i<n; i++) {
            for (int j=0; j<i; j++) {
                int mod = (nums[i]+nums[j]) % k;
                dp[i][mod] = Math.max(dp[i][mod], dp[j][mod] + 1);
                length = Math.max(length, dp[i][mod]);
            }
        }
        return length;
    }
}