class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int c = 3;
        for (int num: arr) {
            if ((num & 1) == 1) {
                c--;
                if (c == 0) return true;
            } else c = 3;
        }
        return false;
    }
}