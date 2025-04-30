class Solution {
    public int findNumbers(int[] nums) {
        int res = 0;
        for (int num: nums)
            if ((Integer.toString(num).length() & 1) == 0)
                res++;
        return res;
    }
}