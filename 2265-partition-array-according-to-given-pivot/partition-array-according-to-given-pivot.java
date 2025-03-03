class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length, j = 0, pivCnt = 0;
        int[] res = new int[n];
        for (int num: nums) {
            if (num < pivot)    res[j++] = num;
            else if (num == pivot)  pivCnt++;
        }
        while (pivCnt-- > 0)    res[j++] = pivot;
        for(int num: nums) if (num > pivot) res[j++] = num;
        return res;
    }
}