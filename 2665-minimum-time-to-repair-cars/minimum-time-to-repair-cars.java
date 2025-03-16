class Solution {
    public long repairCars(int[] ranks, int cars) {
        int n = ranks.length;
        long left = (long)Math.pow(cars / n, 2);
        long res = 0;
        for (int rank : ranks) {
            res = Math.max(res, rank);
        }
        long right = res * (long)Math.pow(Math.ceil((double)cars / n), 2);
        
        while (left <= right) {
            long mid = left + (right - left) / 2;
            if (isPossible(mid, ranks, cars)) {
                res = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }

    private boolean isPossible(long time, int[] ranks, int cars) {
        long k = 0;
        for (int rank : ranks) {
            k += (long)Math.floor(Math.sqrt((double)time / rank));
            if (k >= cars) {
                return true;
            }
        }
        return false;
    }
}