class Solution {
    public int tupleSameProduct(int[] nums) {
        Map<Integer, Integer> hmap = new HashMap<>();
        int n = nums.length, res = 0;
        for (int i=0; i<n-1; i++) {
            for (int j=i+1; j<n; j++) {
                int prod = nums[i]*nums[j];
                hmap.put(prod, hmap.getOrDefault(prod, 0) + 1);
            }
        }
        for (int cnt: hmap.values()) {
            res += 4*(cnt)*(cnt-1);
        }
        return res;
    }
}