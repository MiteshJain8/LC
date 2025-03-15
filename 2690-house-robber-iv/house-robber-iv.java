class Solution {
    public int minCapability(int[] nums, int k) {
        TreeSet<Integer> uniqueNums = new TreeSet<>();
        for (int num : nums) {
            uniqueNums.add(num);
        }
        List<Integer> sizes = new ArrayList<>(uniqueNums);
        int left = 0, right = sizes.size() - 1, res = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (isPossible(nums, k, sizes.get(mid))) {
                res = sizes.get(mid);
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }

    private boolean isPossible(int[] nums, int k, int val) {
        int cur = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= val) {
                cur++;
                if (cur == k) return true;
                i++;
            }
        }
        return false;
    }
}