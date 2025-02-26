class Solution {
    public int maxAbsoluteSum(int[] nums) {
        int curSum = 0, res = 0, minPre = 0, maxPre = 0;
        for (int num: nums) {
            curSum += num;
            res = Math.max(res, Math.max(Math.abs(curSum-minPre), Math.abs(curSum-maxPre)));
            maxPre = Math.max(maxPre, curSum);
            minPre = Math.min(minPre, curSum);
        }
        return res;
    }
}