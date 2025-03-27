class Solution {
    public int minimumIndex(List<Integer> nums) {
        int votes = 0, candidate = -1, n = nums.size();
        for (int i = 0; i < n; i++) {
            if (votes == 0) {
                candidate = nums.get(i);
                votes++;
            } else {
                if (candidate == nums.get(i)) votes++;
                else votes--;
            }
        }
        votes = 0;
        for (int j = 0; j < n; j++) {
            if (nums.get(j) == candidate) {
                votes++;
                if (2*votes > j+1) {
                    if (2*Collections.frequency(nums.subList(j+1, n), candidate) > n-j-1) return j;
                    else return -1; 
                }
            }
        }
        return -1;
    }
}