class Solution {
    public long countBadPairs(int[] nums) {
        Map<Integer, Integer> hmap = new HashMap<>();
        int n = nums.length;
        long res = (long) n * (n - 1) / 2;
        for (int i = 0; i < n; ++i) {
            int key = nums[i] - i;
            hmap.put(key, hmap.getOrDefault(key, 0) + 1);
        }
        for (int cnt : hmap.values()) {
            res -= (long) cnt * (cnt - 1) / 2;
        }
        return res;
    }
}