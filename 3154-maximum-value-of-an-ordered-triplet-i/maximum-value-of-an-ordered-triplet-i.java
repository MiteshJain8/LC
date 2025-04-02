class Solution {
    public long maximumTripletValue(int[] nums) {
        long res = 0, maxi = 0, maxDiff = 0;
        for (int num: nums) {
            res = Math.max(res, maxDiff * num);
            maxDiff = Math.max(maxDiff, maxi - num);
            maxi = Math.max(maxi, num);
        }
        return res;
    }
}