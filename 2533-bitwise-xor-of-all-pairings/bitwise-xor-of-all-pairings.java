class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        int res = 0;
        if ((nums1.length & 1) == 1) 
            res = Arrays.stream(nums2).reduce(0, (x, y) -> x ^ y);
        if ((nums2.length & 1) == 1) 
            res = Arrays.stream(nums1).reduce(res, (x, y) -> x ^ y);
        return res;
    }
}