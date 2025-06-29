class Solution {
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        int M = 1_000_000_007, n = nums.length;
        int[] power = new int[n];
        power[0] = 1;
        for (int i=1; i<n; ++i) power[i] = (power[i-1] * 2) % M;
        int i = 0, j = n-1, res = 0;
        while (i <= j) {
            if (nums[i] + nums[j] <= target) {
                res = (res + power[j-i] % M) % M;
                i++;
            } else j--;
        }
        return res;
    }
}