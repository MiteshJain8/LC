class Solution {
    public int maximumSum(int[] nums) {
        int[] prefix = new int[82];
        int n = nums.length, res = -1;
        for (int i = 0; i < n; ++i) {
            int num = nums[i], dig = 0;
            while (num > 0) {
                dig += num % 10;
                num /= 10;
            }
            if (prefix[dig] > 0) {
                res = Math.max(res, nums[i] + prefix[dig]);
                prefix[dig] = Math.max(nums[i], prefix[dig]);
            } else {
                prefix[dig] = nums[i];
            }
        }
        return res;
    }
}