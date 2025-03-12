class Solution {
    public int lowerBound(int[] nums, int val) {
        int l = 0, r = nums.length-1;
        while (l < r) {
            int mid = l + (r-l)/2;
            if (nums[mid] < val) l = mid+1;
            else r = mid;
        }
        System.out.println(r);
        return r;
    }

    public int maximumCount(int[] nums) {
        int neg, pos = 0, n = nums.length;
        if (nums[n-1] < 0) neg = n;
        else neg = lowerBound(nums, 0);
        if (nums[n-1] > 0) pos = n - lowerBound(nums, 1);
        return Math.max(neg, pos);
    }
}