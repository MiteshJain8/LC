class Solution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] pre_process = new int[n+1];
        int cur_reduction = 0;
        for (int[] q: queries) {
            pre_process[q[0]]++;
            pre_process[q[1]+1]--;
        }
        for (int i=0; i<n; i++) {
            cur_reduction += pre_process[i];
            if (cur_reduction < nums[i]) return false;
        }
        return true;
    }
}