class Solution {
    public int maximumLength(int[] nums) {
        int c = nums[0] & 1, odd = 0, eve = 0, both = 0;
        for (int num: nums) {
            if ((num & 1) == 0) {
                eve++;
            } else {
                odd++;
            }
            if ((num & 1) == c) {
                both++;
                c = 1 - c;
            }
        }
        return Math.max(Math.max(odd, eve), both);
    }
}