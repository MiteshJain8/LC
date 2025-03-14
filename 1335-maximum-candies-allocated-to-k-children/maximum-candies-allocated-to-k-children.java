class Solution {
    public boolean isPossible(int[] candies, long k, int val) {
        long cur = 0;
        int i = candies.length - 1;
        while (i >= 0 && cur < k) {
            if (candies[i] >= val) {
                cur += candies[i]/val;
                i--;
            } else {
                return false;
            }
        }
        return cur >= k;
    }

    public int maximumCandies(int[] candies, long k) {
        long total = 0;
        for (int c: candies) total += c;
        if (total < k) return 0;
        Arrays.sort(candies);
        int left = 1, right = (int)(total/k), res = 0;
        while (left <= right) {
            int mid = left + (right-left)/2;
            if (isPossible(candies, k, mid)) {
                res = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }
}