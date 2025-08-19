class Solution {
    public long zeroFilledSubarray(int[] nums) {
        long res = 0;
        int l = -1;
        for (int r=0; r<nums.length; ++r) {
            if (nums[r] == 0) res += (r-l);
            else l = r;
        }
        return res;
    }
}